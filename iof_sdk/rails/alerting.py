"""Alerting Rail API client."""

from typing import Any, Optional


class AlertingRail:
    """Alerting and threshold management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/alerting"

    def list_alerts(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List alerts."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_alert(self, alert_id: str) -> dict:
        """Get alert by ID."""
        return self.http.get(f"{self.base_path}/{alert_id}")

    def create_alert(self, data: dict) -> dict:
        """Create an alert rule."""
        return self.http.post(self.base_path, json=data)

    def update_alert(self, alert_id: str, data: dict) -> dict:
        """Update an alert rule."""
        return self.http.patch(f"{self.base_path}/{alert_id}", json=data)

    def delete_alert(self, alert_id: str) -> dict:
        """Delete an alert rule."""
        return self.http.delete(f"{self.base_path}/{alert_id}")

    def acknowledge_alert(self, alert_id: str) -> dict:
        """Acknowledge a triggered alert."""
        return self.http.post(f"{self.base_path}/{alert_id}/acknowledge")

    def list_channels(self, page: int = 1, limit: int = 20) -> dict:
        """List alert notification channels."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/channels", params=params)

    def create_channel(self, data: dict) -> dict:
        """Create a notification channel."""
        return self.http.post(f"{self.base_path}/channels", json=data)

    def test_channel(self, channel_id: str) -> dict:
        """Send a test notification to a channel."""
        return self.http.post(f"{self.base_path}/channels/{channel_id}/test")
