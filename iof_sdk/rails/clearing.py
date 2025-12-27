"""Clearing Rail API client."""

from typing import Any, Optional

from ..models import ClearingBatch, PaginatedResponse


class ClearingRail:
    """
    Clearing Rail API client.

    Handles settlement, multilateral netting, and clearing operations.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Clearing rail client."""
        self.http = http_client
        self.base_path = "/api/v1/clearing"

    # Batches
    def list_batches(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List clearing batches.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of clearing batches
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/batches", params=params)

    def get_batch(self, batch_id: str) -> ClearingBatch:
        """
        Get clearing batch by ID.

        Args:
            batch_id: Batch ID

        Returns:
            Clearing batch details
        """
        return self.http.get(f"{self.base_path}/batches/{batch_id}")

    def create_batch(self, data: dict) -> ClearingBatch:
        """
        Create a new clearing batch.

        Args:
            data: Batch creation data

        Returns:
            Created clearing batch
        """
        return self.http.post(f"{self.base_path}/batches", json=data)

    def process_batch(self, batch_id: str) -> ClearingBatch:
        """
        Process a clearing batch.

        Args:
            batch_id: Batch ID

        Returns:
            Processed batch
        """
        return self.http.post(f"{self.base_path}/batches/{batch_id}/process")

    def settle_batch(self, batch_id: str) -> ClearingBatch:
        """
        Settle a clearing batch.

        Args:
            batch_id: Batch ID

        Returns:
            Settled batch
        """
        return self.http.post(f"{self.base_path}/batches/{batch_id}/settle")

    # Transactions
    def list_transactions(
        self,
        page: int = 1,
        limit: int = 20,
        batch_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List clearing transactions.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            batch_id: Filter by batch ID
            status: Filter by status

        Returns:
            Paginated list of transactions
        """
        params = {
            "page": page,
            "limit": limit,
            "batch_id": batch_id,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/transactions", params=params)

    def get_transaction(self, transaction_id: str) -> dict:
        """
        Get clearing transaction by ID.

        Args:
            transaction_id: Transaction ID

        Returns:
            Transaction details
        """
        return self.http.get(f"{self.base_path}/transactions/{transaction_id}")

    # Netting
    def calculate_netting(self, participant_ids: list) -> dict:
        """
        Calculate multilateral netting.

        Args:
            participant_ids: List of participant IDs

        Returns:
            Netting calculation result
        """
        return self.http.post(
            f"{self.base_path}/netting/calculate",
            json={"participant_ids": participant_ids},
        )

    def get_settlement_positions(self, batch_id: str) -> list:
        """
        Get settlement positions for a batch.

        Args:
            batch_id: Batch ID

        Returns:
            List of settlement positions
        """
        return self.http.get(f"{self.base_path}/batches/{batch_id}/positions")
