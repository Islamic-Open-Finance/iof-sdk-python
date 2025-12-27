"""Consent & Privacy Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class ConsentRail:
    """
    Consent & Privacy Rail API client.

    Handles GDPR/CCPA compliance and data privacy management including
    consent tracking, data subject requests, and privacy preferences.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Consent & Privacy rail client."""
        self.http = http_client
        self.base_path = "/api/v1/consent"

    def list_consents(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List privacy consents.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of consents
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/records", params=params)

    def get_consent(self, consent_id: str) -> dict:
        """
        Get consent record by ID.

        Args:
            consent_id: Consent ID

        Returns:
            Consent record details
        """
        return self.http.get(f"{self.base_path}/records/{consent_id}")

    def create_consent(self, data: dict) -> dict:
        """
        Create a new consent record.

        Args:
            data: Consent data

        Returns:
            Created consent record
        """
        return self.http.post(f"{self.base_path}/records", json=data)

    def withdraw_consent(self, consent_id: str) -> dict:
        """
        Withdraw a consent.

        Args:
            consent_id: Consent ID

        Returns:
            Withdrawn consent record
        """
        return self.http.post(f"{self.base_path}/records/{consent_id}/withdraw")

    # Data Subject Requests
    def list_data_subject_requests(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List data subject requests (GDPR/CCPA).

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Request type (access, deletion, portability)
            status: Filter by status

        Returns:
            Paginated list of data subject requests
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/dsr", params=params)

    def get_data_subject_request(self, request_id: str) -> dict:
        """
        Get data subject request by ID.

        Args:
            request_id: Request ID

        Returns:
            Data subject request details
        """
        return self.http.get(f"{self.base_path}/dsr/{request_id}")

    def create_data_subject_request(self, data: dict) -> dict:
        """
        Create a new data subject request.

        Args:
            data: Request data

        Returns:
            Created data subject request
        """
        return self.http.post(f"{self.base_path}/dsr", json=data)

    def fulfill_data_subject_request(self, request_id: str) -> dict:
        """
        Fulfill a data subject request.

        Args:
            request_id: Request ID

        Returns:
            Fulfilled request
        """
        return self.http.post(f"{self.base_path}/dsr/{request_id}/fulfill")
