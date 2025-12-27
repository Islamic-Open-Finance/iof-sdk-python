"""Governance Rail API client."""

from typing import Any, Optional

from ..models import GovernanceBoard, PaginatedResponse


class GovernanceRail:
    """
    Governance Rail API client.

    Handles Shariah board and committee management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Governance rail client."""
        self.http = http_client
        self.base_path = "/api/v1/governance"

    # Boards
    def list_boards(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List governance boards.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by board type

        Returns:
            Paginated list of boards
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
        }
        return self.http.get(f"{self.base_path}/boards", params=params)

    def get_board(self, board_id: str) -> GovernanceBoard:
        """
        Get governance board by ID.

        Args:
            board_id: Board ID

        Returns:
            Board details
        """
        return self.http.get(f"{self.base_path}/boards/{board_id}")

    def create_board(self, data: dict) -> GovernanceBoard:
        """
        Create a new governance board.

        Args:
            data: Board creation data

        Returns:
            Created board
        """
        return self.http.post(f"{self.base_path}/boards", json=data)

    def update_board(self, board_id: str, data: dict) -> GovernanceBoard:
        """
        Update a governance board.

        Args:
            board_id: Board ID
            data: Board update data

        Returns:
            Updated board
        """
        return self.http.patch(f"{self.base_path}/boards/{board_id}", json=data)

    # Members
    def list_members(self, board_id: str) -> list:
        """
        List board members.

        Args:
            board_id: Board ID

        Returns:
            List of board members
        """
        return self.http.get(f"{self.base_path}/boards/{board_id}/members")

    def add_member(self, board_id: str, data: dict) -> dict:
        """
        Add a member to a board.

        Args:
            board_id: Board ID
            data: Member data

        Returns:
            Added member
        """
        return self.http.post(f"{self.base_path}/boards/{board_id}/members", json=data)

    def remove_member(self, board_id: str, member_id: str) -> None:
        """
        Remove a member from a board.

        Args:
            board_id: Board ID
            member_id: Member ID
        """
        self.http.delete(f"{self.base_path}/boards/{board_id}/members/{member_id}")

    # Meetings
    def list_meetings(
        self,
        board_id: str,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List board meetings.

        Args:
            board_id: Board ID
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of meetings
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/boards/{board_id}/meetings", params=params)

    def create_meeting(self, board_id: str, data: dict) -> dict:
        """
        Schedule a board meeting.

        Args:
            board_id: Board ID
            data: Meeting data

        Returns:
            Created meeting
        """
        return self.http.post(f"{self.base_path}/boards/{board_id}/meetings", json=data)

    def get_meeting(self, board_id: str, meeting_id: str) -> dict:
        """
        Get meeting details.

        Args:
            board_id: Board ID
            meeting_id: Meeting ID

        Returns:
            Meeting details
        """
        return self.http.get(f"{self.base_path}/boards/{board_id}/meetings/{meeting_id}")

    # Resolutions
    def list_resolutions(
        self,
        board_id: str,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List board resolutions.

        Args:
            board_id: Board ID
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of resolutions
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/boards/{board_id}/resolutions", params=params)

    def create_resolution(self, board_id: str, data: dict) -> dict:
        """
        Create a board resolution.

        Args:
            board_id: Board ID
            data: Resolution data

        Returns:
            Created resolution
        """
        return self.http.post(f"{self.base_path}/boards/{board_id}/resolutions", json=data)
