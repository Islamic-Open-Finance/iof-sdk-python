"""Disputes & Collections Rail API client."""

from typing import Any, Optional

from ..models import Dispute, PaginatedResponse


class DisputesRail:
    """
    Disputes & Collections Rail API client.

    Handles dispute management and debt collection processes.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Disputes rail client."""
        self.http = http_client
        self.base_path = "/api/v1/disputes"

    def list_disputes(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List disputes with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            type: Filter by dispute type

        Returns:
            Paginated list of disputes
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
        }
        return self.http.get(self.base_path, params=params)

    def get_dispute(self, dispute_id: str) -> Dispute:
        """
        Get dispute by ID.

        Args:
            dispute_id: Dispute ID

        Returns:
            Dispute details
        """
        return self.http.get(f"{self.base_path}/{dispute_id}")

    def create_dispute(self, data: dict) -> Dispute:
        """
        Create a new dispute.

        Args:
            data: Dispute creation data

        Returns:
            Created dispute
        """
        return self.http.post(self.base_path, json=data)

    def update_dispute(self, dispute_id: str, data: dict) -> Dispute:
        """
        Update a dispute.

        Args:
            dispute_id: Dispute ID
            data: Dispute update data

        Returns:
            Updated dispute
        """
        return self.http.patch(f"{self.base_path}/{dispute_id}", json=data)

    def resolve_dispute(self, dispute_id: str, resolution: str) -> Dispute:
        """
        Resolve a dispute.

        Args:
            dispute_id: Dispute ID
            resolution: Resolution details

        Returns:
            Resolved dispute
        """
        return self.http.post(
            f"{self.base_path}/{dispute_id}/resolve", json={"resolution": resolution}
        )

    def escalate_dispute(self, dispute_id: str, reason: str) -> Dispute:
        """
        Escalate a dispute.

        Args:
            dispute_id: Dispute ID
            reason: Escalation reason

        Returns:
            Escalated dispute
        """
        return self.http.post(
            f"{self.base_path}/{dispute_id}/escalate", json={"reason": reason}
        )

    # Collections
    def list_collections(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List collection cases.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of collections
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/collections", params=params)

    def get_collection(self, collection_id: str) -> dict:
        """
        Get collection case by ID.

        Args:
            collection_id: Collection ID

        Returns:
            Collection case details
        """
        return self.http.get(f"{self.base_path}/collections/{collection_id}")

    def create_collection(self, data: dict) -> dict:
        """
        Create a new collection case.

        Args:
            data: Collection case data

        Returns:
            Created collection case
        """
        return self.http.post(f"{self.base_path}/collections", json=data)
