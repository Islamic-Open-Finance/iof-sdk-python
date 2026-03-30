"""Limits & Controls Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class LimitsRail:
    """
    Limits & Controls Rail API client.

    Provides transaction limits and controls:
    - Limit definitions and management
    - Real-time limit checking
    - Utilization tracking
    - Approval workflows (4-eyes)
    - Breach detection and handling
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Limits rail client."""
        self.http = http_client
        self.base_path = "/api/v1/limits"

    # Limit Management

    def list_limits(
        self,
        page: int = 1,
        limit: int = 20,
        limit_type: Optional[str] = None,
        scope: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List limits.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            limit_type: Filter by type (transaction, daily, weekly, etc.)
            scope: Filter by scope (global, tenant, user, etc.)
            status: Filter by status

        Returns:
            Paginated list of limits
        """
        params = {
            "page": page,
            "limit": limit,
            "type": limit_type,
            "scope": scope,
            "status": status,
        }
        return self.http.get(self.base_path, params=params)

    def create_limit(self, data: dict) -> dict:
        """
        Create a new limit.

        Args:
            data: Limit data (name, type, scope, amount, currency)

        Returns:
            Created limit
        """
        return self.http.post(self.base_path, json=data)

    def get_limit(self, limit_id: str) -> dict:
        """
        Get limit by ID.

        Args:
            limit_id: Limit ID

        Returns:
            Limit details
        """
        return self.http.get(f"{self.base_path}/{limit_id}")

    def update_limit(self, limit_id: str, data: dict) -> dict:
        """
        Update a limit.

        Args:
            limit_id: Limit ID
            data: Update data

        Returns:
            Updated limit
        """
        return self.http.patch(f"{self.base_path}/{limit_id}", json=data)

    def delete_limit(self, limit_id: str) -> None:
        """
        Delete a limit.

        Args:
            limit_id: Limit ID
        """
        self.http.delete(f"{self.base_path}/{limit_id}")

    # Limit Checking

    def check_limit(self, data: dict) -> dict:
        """
        Check if a transaction is within limits.

        Args:
            data: Check input (amount, currency, scope, scopeId, etc.)

        Returns:
            Check result (allowed, denied, or requires_approval)
        """
        return self.http.post(f"{self.base_path}/check", json=data)

    def record_usage(self, data: dict) -> dict:
        """
        Record limit usage for a transaction.

        Args:
            data: Usage data (limitId, amount, transactionId)

        Returns:
            Updated utilization
        """
        return self.http.post(f"{self.base_path}/usage", json=data)

    # Utilization

    def get_utilization(self) -> dict:
        """
        Get all limit utilizations.

        Returns:
            List of limit utilizations
        """
        return self.http.get(f"{self.base_path}/utilization")

    def get_limit_utilization(self, limit_id: str) -> dict:
        """
        Get utilization for a specific limit.

        Args:
            limit_id: Limit ID

        Returns:
            Limit utilization details
        """
        return self.http.get(f"{self.base_path}/utilization/{limit_id}")

    # Approvals

    def list_approvals(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        limit_id: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List approval requests.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            limit_id: Filter by limit ID

        Returns:
            Paginated list of approval requests
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "limitId": limit_id,
        }
        return self.http.get(f"{self.base_path}/approvals", params=params)

    def create_approval(self, data: dict) -> dict:
        """
        Create an approval request.

        Args:
            data: Approval data (limitId, amount, currency, reason)

        Returns:
            Created approval request
        """
        return self.http.post(f"{self.base_path}/approvals", json=data)

    def get_approval(self, approval_id: str) -> dict:
        """
        Get approval request by ID.

        Args:
            approval_id: Approval ID

        Returns:
            Approval request details
        """
        return self.http.get(f"{self.base_path}/approvals/{approval_id}")

    def approve_request(self, approval_id: str, data: dict) -> dict:
        """
        Approve an approval request.

        Args:
            approval_id: Approval ID
            data: Approval data (decision, comment)

        Returns:
            Updated approval request
        """
        return self.http.post(
            f"{self.base_path}/approvals/{approval_id}/approve", json=data
        )

    def reject_request(self, approval_id: str, data: dict) -> dict:
        """
        Reject an approval request.

        Args:
            approval_id: Approval ID
            data: Rejection data (decision, comment)

        Returns:
            Updated approval request
        """
        return self.http.post(
            f"{self.base_path}/approvals/{approval_id}/reject", json=data
        )

    # Breaches

    def list_breaches(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        severity: Optional[str] = None,
        limit_id: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List limit breaches.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            severity: Filter by severity
            limit_id: Filter by limit ID

        Returns:
            Paginated list of breaches
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "severity": severity,
            "limitId": limit_id,
        }
        return self.http.get(f"{self.base_path}/breaches", params=params)

    def get_breach(self, breach_id: str) -> dict:
        """
        Get breach by ID.

        Args:
            breach_id: Breach ID

        Returns:
            Breach details
        """
        return self.http.get(f"{self.base_path}/breaches/{breach_id}")

    def acknowledge_breach(self, breach_id: str) -> dict:
        """
        Acknowledge a breach.

        Args:
            breach_id: Breach ID

        Returns:
            Acknowledged breach
        """
        return self.http.post(
            f"{self.base_path}/breaches/{breach_id}/acknowledge"
        )

    def resolve_breach(self, breach_id: str, resolution_notes: str) -> dict:
        """
        Resolve a breach.

        Args:
            breach_id: Breach ID
            resolution_notes: Resolution notes

        Returns:
            Resolved breach
        """
        return self.http.post(
            f"{self.base_path}/breaches/{breach_id}/resolve",
            json={"resolutionNotes": resolution_notes},
        )
