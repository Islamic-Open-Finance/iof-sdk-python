"""Message Rail API client."""

from typing import Any, Optional

from ..models import Message, PaginatedResponse


class MessagesRail:
    """
    Message Rail API client.

    Handles ISO 20022 messaging for Islamic finance transactions.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Messages rail client."""
        self.http = http_client
        self.base_path = "/api/v1/messages"

    def list_messages(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        direction: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List messages with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by message type
            direction: Filter by direction (inbound/outbound)
            status: Filter by status

        Returns:
            Paginated list of messages
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "direction": direction,
            "status": status,
        }
        return self.http.get(self.base_path, params=params)

    def get_message(self, message_id: str) -> Message:
        """
        Get message by ID.

        Args:
            message_id: Message ID

        Returns:
            Message details
        """
        return self.http.get(f"{self.base_path}/{message_id}")

    def create_message(self, data: dict) -> Message:
        """
        Create and send a new message.

        Args:
            data: Message data

        Returns:
            Created message
        """
        return self.http.post(self.base_path, json=data)

    def parse_message(self, raw_message: str) -> dict:
        """
        Parse an ISO 20022 message.

        Args:
            raw_message: Raw message content

        Returns:
            Parsed message structure
        """
        return self.http.post(
            f"{self.base_path}/parse", json={"message": raw_message}
        )

    def validate_message(self, data: dict) -> dict:
        """
        Validate a message without sending.

        Args:
            data: Message data

        Returns:
            Validation result
        """
        return self.http.post(f"{self.base_path}/validate", json=data)

    def get_message_status(self, message_id: str) -> dict:
        """
        Get message delivery status.

        Args:
            message_id: Message ID

        Returns:
            Message status
        """
        return self.http.get(f"{self.base_path}/{message_id}/status")
