"""Reconciliation Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, ReconciliationException, ReconciliationJob


class ReconciliationRail:
    """
    Reconciliation Rail API client.

    Handles transaction reconciliation, matching, and exception management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Reconciliation rail client."""
        self.http = http_client
        self.base_path = "/api/v1/reconciliation"

    # Jobs
    def list_jobs(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List reconciliation jobs.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of reconciliation jobs
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/jobs", params=params)

    def get_job(self, job_id: str) -> ReconciliationJob:
        """
        Get reconciliation job by ID.

        Args:
            job_id: Job ID

        Returns:
            Reconciliation job details
        """
        return self.http.get(f"{self.base_path}/jobs/{job_id}")

    def create_job(self, data: dict) -> ReconciliationJob:
        """
        Create a new reconciliation job.

        Args:
            data: Job creation data

        Returns:
            Created reconciliation job
        """
        return self.http.post(f"{self.base_path}/jobs", json=data)

    def start_job(self, job_id: str) -> ReconciliationJob:
        """
        Start a reconciliation job.

        Args:
            job_id: Job ID

        Returns:
            Started job
        """
        return self.http.post(f"{self.base_path}/jobs/{job_id}/start")

    def cancel_job(self, job_id: str) -> ReconciliationJob:
        """
        Cancel a reconciliation job.

        Args:
            job_id: Job ID

        Returns:
            Cancelled job
        """
        return self.http.post(f"{self.base_path}/jobs/{job_id}/cancel")

    # Exceptions
    def list_exceptions(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List reconciliation exceptions.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            type: Filter by exception type

        Returns:
            Paginated list of exceptions
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
        }
        return self.http.get(f"{self.base_path}/exceptions", params=params)

    def get_exception(self, exception_id: str) -> ReconciliationException:
        """
        Get reconciliation exception by ID.

        Args:
            exception_id: Exception ID

        Returns:
            Exception details
        """
        return self.http.get(f"{self.base_path}/exceptions/{exception_id}")

    def resolve_exception(
        self, exception_id: str, resolution: str
    ) -> ReconciliationException:
        """
        Resolve a reconciliation exception.

        Args:
            exception_id: Exception ID
            resolution: Resolution details

        Returns:
            Resolved exception
        """
        return self.http.post(
            f"{self.base_path}/exceptions/{exception_id}/resolve",
            json={"resolution": resolution},
        )

    def dismiss_exception(self, exception_id: str, reason: str) -> ReconciliationException:
        """
        Dismiss a reconciliation exception.

        Args:
            exception_id: Exception ID
            reason: Dismissal reason

        Returns:
            Dismissed exception
        """
        return self.http.post(
            f"{self.base_path}/exceptions/{exception_id}/dismiss",
            json={"reason": reason},
        )

    # Matching
    def match_transactions(self, source_id: str, target_id: str) -> dict:
        """
        Manually match two transactions.

        Args:
            source_id: Source transaction ID
            target_id: Target transaction ID

        Returns:
            Match result
        """
        return self.http.post(
            f"{self.base_path}/match",
            json={"source_id": source_id, "target_id": target_id},
        )
