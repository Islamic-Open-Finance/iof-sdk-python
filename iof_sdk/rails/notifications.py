"""Notifications Rail API client."""

from typing import Any, Optional

from ..models import Notification, PaginatedResponse


class NotificationsRail:
    """
    Notifications Rail API client.

    Handles multi-channel notifications (email, SMS, push, etc.).
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Notifications rail client."""
        self.http = http_client
        self.base_path = "/api/v1/notifications"

    def list_notifications(
        self,
        page: int = 1,
        limit: int = 20,
        channel: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List notifications with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            channel: Filter by channel (email, sms, push)
            status: Filter by status

        Returns:
            Paginated list of notifications
        """
        params = {
            "page": page,
            "limit": limit,
            "channel": channel,
            "status": status,
        }
        return self.http.get(self.base_path, params=params)

    def get_notification(self, notification_id: str) -> Notification:
        """
        Get notification by ID.

        Args:
            notification_id: Notification ID

        Returns:
            Notification details
        """
        return self.http.get(f"{self.base_path}/{notification_id}")

    def send_notification(self, data: dict) -> Notification:
        """
        Send a new notification.

        Args:
            data: Notification data

        Returns:
            Sent notification
        """
        return self.http.post(self.base_path, json=data)

    def send_email(self, data: dict) -> Notification:
        """
        Send an email notification.

        Args:
            data: Email data (recipient, subject, body)

        Returns:
            Sent notification
        """
        return self.http.post(f"{self.base_path}/email", json=data)

    def send_sms(self, data: dict) -> Notification:
        """
        Send an SMS notification.

        Args:
            data: SMS data (recipient, body)

        Returns:
            Sent notification
        """
        return self.http.post(f"{self.base_path}/sms", json=data)

    def send_push(self, data: dict) -> Notification:
        """
        Send a push notification.

        Args:
            data: Push notification data

        Returns:
            Sent notification
        """
        return self.http.post(f"{self.base_path}/push", json=data)

    # Templates
    def list_templates(
        self,
        page: int = 1,
        limit: int = 20,
        channel: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List notification templates.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            channel: Filter by channel

        Returns:
            Paginated list of templates
        """
        params = {
            "page": page,
            "limit": limit,
            "channel": channel,
        }
        return self.http.get(f"{self.base_path}/templates", params=params)

    def get_template(self, template_id: str) -> dict:
        """
        Get notification template by ID.

        Args:
            template_id: Template ID

        Returns:
            Template details
        """
        return self.http.get(f"{self.base_path}/templates/{template_id}")

    def send_from_template(self, template_id: str, data: dict) -> Notification:
        """
        Send notification from template.

        Args:
            template_id: Template ID
            data: Template variables and recipient

        Returns:
            Sent notification
        """
        return self.http.post(
            f"{self.base_path}/templates/{template_id}/send", json=data
        )

    # Preferences
    def get_preferences(self, user_id: str) -> dict:
        """
        Get user notification preferences.

        Args:
            user_id: User ID

        Returns:
            User preferences
        """
        return self.http.get(f"{self.base_path}/preferences/{user_id}")

    def update_preferences(self, user_id: str, data: dict) -> dict:
        """
        Update user notification preferences.

        Args:
            user_id: User ID
            data: Preferences data

        Returns:
            Updated preferences
        """
        return self.http.put(f"{self.base_path}/preferences/{user_id}", json=data)
