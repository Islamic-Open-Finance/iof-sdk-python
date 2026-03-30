"""Notification Hub Rail API client."""

from typing import Any, Optional


class NotificationHubRail:
    """Centralised multi-channel notification hub rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/notification-hub"

    def list_notifications(self, page: int = 1, limit: int = 20, channel: Optional[str] = None) -> dict:
        """List notifications."""
        params = {"page": page, "limit": limit, "channel": channel}
        return self.http.get(self.base_path, params=params)

    def get_notification(self, notification_id: str) -> dict:
        """Get notification by ID."""
        return self.http.get(f"{self.base_path}/{notification_id}")

    def send_notification(self, data: dict) -> dict:
        """Send a notification via one or more channels."""
        return self.http.post(self.base_path, json=data)

    def send_bulk(self, data: dict) -> dict:
        """Send bulk notifications."""
        return self.http.post(f"{self.base_path}/bulk", json=data)

    def list_templates(self, page: int = 1, limit: int = 20) -> dict:
        """List notification templates."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/templates", params=params)

    def get_template(self, template_id: str) -> dict:
        """Get notification template by ID."""
        return self.http.get(f"{self.base_path}/templates/{template_id}")

    def create_template(self, data: dict) -> dict:
        """Create a notification template."""
        return self.http.post(f"{self.base_path}/templates", json=data)

    def update_template(self, template_id: str, data: dict) -> dict:
        """Update a notification template."""
        return self.http.patch(f"{self.base_path}/templates/{template_id}", json=data)

    def get_delivery_status(self, notification_id: str) -> dict:
        """Get delivery status of a notification."""
        return self.http.get(f"{self.base_path}/{notification_id}/status")

    def list_preferences(self, recipient_id: str) -> dict:
        """Get notification preferences for a recipient."""
        return self.http.get(f"{self.base_path}/preferences/{recipient_id}")

    def update_preferences(self, recipient_id: str, data: dict) -> dict:
        """Update notification preferences for a recipient."""
        return self.http.patch(f"{self.base_path}/preferences/{recipient_id}", json=data)
