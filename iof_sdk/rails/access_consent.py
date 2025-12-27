"""Access & Consent Rail API client."""

from typing import Any, Optional

from ..models import Consent, CreateConsentRequest, PaginatedResponse


class AccessConsentRail:
    """
    Access & Consent Rail API client.

    Handles Open Banking consent management for AISP (Account Information
    Service Provider) and PISP (Payment Initiation Service Provider).
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Access Consent rail client."""
        self.http = http_client
        self.base_path = "/api/v1/access/consents"

    def list_consents(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List consents with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status (e.g., "ACTIVE", "REVOKED")
            type: Filter by type (e.g., "AISP", "PISP")

        Returns:
            Paginated list of consents
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
        }
        return self.http.get(self.base_path, params=params)

    def get_consent(self, consent_id: str) -> Consent:
        """
        Get consent by ID.

        Args:
            consent_id: Consent ID

        Returns:
            Consent details
        """
        return self.http.get(f"{self.base_path}/{consent_id}")

    def create_consent(self, data: CreateConsentRequest) -> Consent:
        """
        Create a new consent.

        Args:
            data: Consent creation data

        Returns:
            Created consent
        """
        return self.http.post(self.base_path, json=data)

    def revoke_consent(self, consent_id: str) -> Consent:
        """
        Revoke a consent.

        Args:
            consent_id: Consent ID

        Returns:
            Revoked consent
        """
        return self.http.post(f"{self.base_path}/{consent_id}/revoke")

    def renew_consent(self, consent_id: str) -> Consent:
        """
        Renew a consent.

        Args:
            consent_id: Consent ID

        Returns:
            Renewed consent
        """
        return self.http.post(f"{self.base_path}/{consent_id}/renew")
