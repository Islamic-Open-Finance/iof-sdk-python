"""
HTTP client and main IOF SDK client.

This module provides the core HTTP client functionality and the main
IOFClient class that provides access to all rail APIs.
"""

import time
from typing import Any, Dict, Optional, Union
from urllib.parse import urlencode, urljoin

import httpx

from .exceptions import (
    ConnectionError as IOFConnectionError,
    TimeoutError as IOFTimeoutError,
    create_api_error,
)


class HttpClient:
    """
    HTTP client for making requests to the IOF API.

    Handles authentication, retries, timeouts, and error handling.
    """

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        access_token: Optional[str] = None,
        tenant_id: Optional[str] = None,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        """
        Initialize the HTTP client.

        Args:
            base_url: Base URL of the IOF API
            api_key: API key for authentication
            access_token: Bearer token for authentication
            tenant_id: Tenant ID for multi-tenancy
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

        # Build default headers
        self.headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        if api_key:
            self.headers["X-Api-Key"] = api_key

        if access_token:
            self.headers["Authorization"] = f"Bearer {access_token}"

        if tenant_id:
            self.headers["X-Tenant-Id"] = tenant_id

        # Create httpx client
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=self.timeout,
        )

    def __enter__(self) -> "HttpClient":
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self.client.close()

    def set_api_key(self, api_key: str) -> None:
        """
        Set the API key for authentication.

        Args:
            api_key: API key
        """
        self.headers["X-Api-Key"] = api_key
        self.client.headers["X-Api-Key"] = api_key

    def set_access_token(self, access_token: str) -> None:
        """
        Set the bearer token for authentication.

        Args:
            access_token: Bearer token
        """
        self.headers["Authorization"] = f"Bearer {access_token}"
        self.client.headers["Authorization"] = f"Bearer {access_token}"

    def set_tenant_id(self, tenant_id: str) -> None:
        """
        Set the tenant ID for multi-tenancy.

        Args:
            tenant_id: Tenant ID
        """
        self.headers["X-Tenant-Id"] = tenant_id
        self.client.headers["X-Tenant-Id"] = tenant_id

    def _build_url(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Build full URL with query parameters.

        Args:
            path: URL path
            params: Query parameters

        Returns:
            Full URL string
        """
        url = path if path.startswith("http") else urljoin(self.base_url, path)

        if params:
            # Filter out None values
            filtered_params = {k: v for k, v in params.items() if v is not None}
            if filtered_params:
                query_string = urlencode(filtered_params, doseq=True)
                url = f"{url}?{query_string}"

        return url

    def _make_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Make HTTP request with retry logic.

        Args:
            method: HTTP method
            path: URL path
            params: Query parameters
            json: JSON body
            headers: Additional headers

        Returns:
            Response data

        Raises:
            ApiError: If the API returns an error
            TimeoutError: If the request times out
            ConnectionError: If the connection fails
        """
        url = self._build_url(path, params)
        request_headers = {**self.headers, **(headers or {})}

        last_exception: Optional[Exception] = None

        for attempt in range(self.max_retries):
            try:
                response = self.client.request(
                    method=method,
                    url=url,
                    json=json,
                    headers=request_headers,
                )

                # Handle successful responses
                if response.status_code == 204:
                    return None

                if 200 <= response.status_code < 300:
                    if response.content:
                        return response.json()
                    return None

                # Handle error responses
                try:
                    error_data = response.json()
                    error_message = error_data.get("error", {}).get(
                        "message", response.text
                    )
                    error_code = error_data.get("error", {}).get("code")
                    error_details = error_data.get("error", {}).get("details")
                except Exception:
                    error_message = response.text or response.reason_phrase
                    error_code = None
                    error_details = None

                error = create_api_error(
                    status_code=response.status_code,
                    message=error_message,
                    code=error_code,
                    details=error_details,
                )

                # Don't retry client errors (4xx)
                if 400 <= response.status_code < 500:
                    raise error

                last_exception = error

            except httpx.TimeoutException as e:
                last_exception = IOFTimeoutError(f"Request timeout: {str(e)}")
            except httpx.NetworkError as e:
                last_exception = IOFConnectionError(f"Connection failed: {str(e)}")
            except httpx.HTTPStatusError as e:
                last_exception = create_api_error(
                    status_code=e.response.status_code,
                    message=str(e),
                )

            # Wait before retrying with exponential backoff
            if attempt < self.max_retries - 1:
                wait_time = 2**attempt
                time.sleep(wait_time)

        # Raise the last exception if all retries failed
        if last_exception:
            raise last_exception

        raise IOFConnectionError("Request failed after all retries")

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Make GET request.

        Args:
            path: URL path
            params: Query parameters
            headers: Additional headers

        Returns:
            Response data
        """
        return self._make_request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Make POST request.

        Args:
            path: URL path
            json: JSON body
            params: Query parameters
            headers: Additional headers

        Returns:
            Response data
        """
        return self._make_request(
            "POST", path, params=params, json=json, headers=headers
        )

    def put(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Make PUT request.

        Args:
            path: URL path
            json: JSON body
            params: Query parameters
            headers: Additional headers

        Returns:
            Response data
        """
        return self._make_request(
            "PUT", path, params=params, json=json, headers=headers
        )

    def patch(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Make PATCH request.

        Args:
            path: URL path
            json: JSON body
            params: Query parameters
            headers: Additional headers

        Returns:
            Response data
        """
        return self._make_request(
            "PATCH", path, params=params, json=json, headers=headers
        )

    def delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Make DELETE request.

        Args:
            path: URL path
            params: Query parameters
            headers: Additional headers

        Returns:
            Response data
        """
        return self._make_request("DELETE", path, params=params, headers=headers)


class IOFClient:
    """
    Main client for the Islamic Open Finance API.

    Provides access to all rail APIs through properties.

    Example:
        >>> client = IOFClient(
        ...     base_url="https://api.example.com",
        ...     api_key="your-api-key",
        ...     tenant_id="tenant-123"
        ... )
        >>> contracts = client.contracts.list_contracts(status="ACTIVE")
        >>> alert = client.aml.create_alert(...)
    """

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        access_token: Optional[str] = None,
        tenant_id: Optional[str] = None,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        """
        Initialize the IOF client.

        Args:
            base_url: Base URL of the IOF API
            api_key: API key for authentication
            access_token: Bearer token for authentication
            tenant_id: Tenant ID for multi-tenancy
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.http = HttpClient(
            base_url=base_url,
            api_key=api_key,
            access_token=access_token,
            tenant_id=tenant_id,
            timeout=timeout,
            max_retries=max_retries,
        )

        # Import rail clients lazily to avoid circular imports
        from .rails.contracts import ContractsRail
        from .rails.jurisdictions import JurisdictionsRail
        from .rails.access_consent import AccessConsentRail
        from .rails.kyc import KycRail
        from .rails.aml import AmlRail
        from .rails.consent import ConsentRail
        from .rails.developer import DeveloperRail
        from .rails.partners import PartnersRail
        from .rails.cases import CasesRail
        from .rails.disputes import DisputesRail
        from .rails.zakat import ZakatRail
        from .rails.reconciliation import ReconciliationRail
        from .rails.routing import RoutingRail
        from .rails.messages import MessagesRail
        from .rails.clearing import ClearingRail
        from .rails.treasury import TreasuryRail
        from .rails.risk import RiskRail
        from .rails.portfolio import PortfolioRail
        from .rails.reporting import ReportingRail
        from .rails.analytics import AnalyticsRail
        from .rails.legal import LegalRail
        from .rails.underwriting import UnderwritingRail
        from .rails.compliance import ComplianceRail
        from .rails.governance import GovernanceRail
        from .rails.events import EventsRail
        from .rails.notifications import NotificationsRail
        from .rails.search import SearchRail
        from .rails.webhooks import WebhooksRail
        from .rails.observability import ObservabilityRail

        # Initialize all rail clients
        self._contracts = ContractsRail(self.http)
        self._jurisdictions = JurisdictionsRail(self.http)
        self._access_consent = AccessConsentRail(self.http)
        self._kyc = KycRail(self.http)
        self._aml = AmlRail(self.http)
        self._consent = ConsentRail(self.http)
        self._developer = DeveloperRail(self.http)
        self._partners = PartnersRail(self.http)
        self._cases = CasesRail(self.http)
        self._disputes = DisputesRail(self.http)
        self._zakat = ZakatRail(self.http)
        self._reconciliation = ReconciliationRail(self.http)
        self._routing = RoutingRail(self.http)
        self._messages = MessagesRail(self.http)
        self._clearing = ClearingRail(self.http)
        self._treasury = TreasuryRail(self.http)
        self._risk = RiskRail(self.http)
        self._portfolio = PortfolioRail(self.http)
        self._reporting = ReportingRail(self.http)
        self._analytics = AnalyticsRail(self.http)
        self._legal = LegalRail(self.http)
        self._underwriting = UnderwritingRail(self.http)
        self._compliance = ComplianceRail(self.http)
        self._governance = GovernanceRail(self.http)
        self._events = EventsRail(self.http)
        self._notifications = NotificationsRail(self.http)
        self._search = SearchRail(self.http)
        self._webhooks = WebhooksRail(self.http)
        self._observability = ObservabilityRail(self.http)

    def __enter__(self) -> "IOFClient":
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the client."""
        self.http.close()

    # Rail properties

    @property
    def contracts(self):
        """Access the Contracts rail."""
        return self._contracts

    @property
    def jurisdictions(self):
        """Access the Jurisdictions rail."""
        return self._jurisdictions

    @property
    def access_consent(self):
        """Access the Access Consent rail."""
        return self._access_consent

    @property
    def kyc(self):
        """Access the KYC rail."""
        return self._kyc

    @property
    def aml(self):
        """Access the AML rail."""
        return self._aml

    @property
    def consent(self):
        """Access the Consent & Privacy rail."""
        return self._consent

    @property
    def developer(self):
        """Access the Developer rail."""
        return self._developer

    @property
    def partners(self):
        """Access the Partners rail."""
        return self._partners

    @property
    def cases(self):
        """Access the Cases rail."""
        return self._cases

    @property
    def disputes(self):
        """Access the Disputes rail."""
        return self._disputes

    @property
    def zakat(self):
        """Access the Zakat rail."""
        return self._zakat

    @property
    def reconciliation(self):
        """Access the Reconciliation rail."""
        return self._reconciliation

    @property
    def routing(self):
        """Access the Routing rail."""
        return self._routing

    @property
    def messages(self):
        """Access the Messages rail."""
        return self._messages

    @property
    def clearing(self):
        """Access the Clearing rail."""
        return self._clearing

    @property
    def treasury(self):
        """Access the Treasury rail."""
        return self._treasury

    @property
    def risk(self):
        """Access the Risk rail."""
        return self._risk

    @property
    def portfolio(self):
        """Access the Portfolio rail."""
        return self._portfolio

    @property
    def reporting(self):
        """Access the Reporting rail."""
        return self._reporting

    @property
    def analytics(self):
        """Access the Analytics rail."""
        return self._analytics

    @property
    def legal(self):
        """Access the Legal rail."""
        return self._legal

    @property
    def underwriting(self):
        """Access the Underwriting rail."""
        return self._underwriting

    @property
    def compliance(self):
        """Access the Compliance rail."""
        return self._compliance

    @property
    def governance(self):
        """Access the Governance rail."""
        return self._governance

    @property
    def events(self):
        """Access the Events rail."""
        return self._events

    @property
    def notifications(self):
        """Access the Notifications rail."""
        return self._notifications

    @property
    def search(self):
        """Access the Search rail."""
        return self._search

    @property
    def webhooks(self):
        """Access the Webhooks rail."""
        return self._webhooks

    @property
    def observability(self):
        """Access the Observability rail."""
        return self._observability
