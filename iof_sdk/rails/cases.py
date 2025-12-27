"""Cases Rail API client."""

from typing import Any, Optional

from ..models import Case, PaginatedResponse


class CasesRail:
    """
    Cases Rail API client.

    Handles case management for operations, disputes, and investigations.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Cases rail client."""
        self.http = http_client
        self.base_path = "/api/v1/cases"

    def list_cases(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
        priority: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List cases with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            type: Filter by case type
            priority: Filter by priority

        Returns:
            Paginated list of cases
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
            "priority": priority,
        }
        return self.http.get(self.base_path, params=params)

    def get_case(self, case_id: str) -> Case:
        """
        Get case by ID.

        Args:
            case_id: Case ID

        Returns:
            Case details
        """
        return self.http.get(f"{self.base_path}/{case_id}")

    def create_case(self, data: dict) -> Case:
        """
        Create a new case.

        Args:
            data: Case creation data

        Returns:
            Created case
        """
        return self.http.post(self.base_path, json=data)

    def update_case(self, case_id: str, data: dict) -> Case:
        """
        Update a case.

        Args:
            case_id: Case ID
            data: Case update data

        Returns:
            Updated case
        """
        return self.http.patch(f"{self.base_path}/{case_id}", json=data)

    def assign_case(self, case_id: str, assignee_id: str) -> Case:
        """
        Assign a case to a user.

        Args:
            case_id: Case ID
            assignee_id: User ID to assign to

        Returns:
            Assigned case
        """
        return self.http.post(
            f"{self.base_path}/{case_id}/assign", json={"assignee_id": assignee_id}
        )

    def close_case(self, case_id: str, resolution: str) -> Case:
        """
        Close a case.

        Args:
            case_id: Case ID
            resolution: Case resolution

        Returns:
            Closed case
        """
        return self.http.post(
            f"{self.base_path}/{case_id}/close", json={"resolution": resolution}
        )

    def add_comment(self, case_id: str, comment: str) -> dict:
        """
        Add a comment to a case.

        Args:
            case_id: Case ID
            comment: Comment text

        Returns:
            Created comment
        """
        return self.http.post(
            f"{self.base_path}/{case_id}/comments", json={"comment": comment}
        )

    def get_case_history(self, case_id: str) -> list:
        """
        Get case history.

        Args:
            case_id: Case ID

        Returns:
            List of case history entries
        """
        return self.http.get(f"{self.base_path}/{case_id}/history")
