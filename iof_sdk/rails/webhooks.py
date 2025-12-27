"""Webhooks Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, Webhook


class WebhooksRail:
    """
    Webhooks Rail API client.

    Handles webhook endpoint management and delivery monitoring.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Webhooks rail client."""
        self.http = http_client
        self.base_path = "/api/v1/webhooks"

    def list_webhooks(
        self,
        page: int = 1,
        limit: int = 20,
        enabled: Optional[bool] = None,
    ) -> PaginatedResponse:
        """
        List webhook endpoints.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            enabled: Filter by enabled status

        Returns:
            Paginated list of webhooks
        """
        params = {
            "page": page,
            "limit": limit,
            "enabled": enabled,
        }
        return self.http.get(self.base_path, params=params)

    def get_webhook(self, webhook_id: str) -> Webhook:
        """
        Get webhook by ID.

        Args:
            webhook_id: Webhook ID

        Returns:
            Webhook details
        """
        return self.http.get(f"{self.base_path}/{webhook_id}")

    def create_webhook(self, data: dict) -> Webhook:
        """
        Create a new webhook endpoint.

        Args:
            data: Webhook creation data (url, events, secret)

        Returns:
            Created webhook
        """
        return self.http.post(self.base_path, json=data)

    def update_webhook(self, webhook_id: str, data: dict) -> Webhook:
        """
        Update a webhook endpoint.

        Args:
            webhook_id: Webhook ID
            data: Webhook update data

        Returns:
            Updated webhook
        """
        return self.http.patch(f"{self.base_path}/{webhook_id}", json=data)

    def delete_webhook(self, webhook_id: str) -> None:
        """
        Delete a webhook endpoint.

        Args:
            webhook_id: Webhook ID
        """
        self.http.delete(f"{self.base_path}/{webhook_id}")

    def enable_webhook(self, webhook_id: str) -> Webhook:
        """
        Enable a webhook endpoint.

        Args:
            webhook_id: Webhook ID

        Returns:
            Enabled webhook
        """
        return self.http.post(f"{self.base_path}/{webhook_id}/enable")

    def disable_webhook(self, webhook_id: str) -> Webhook:
        """
        Disable a webhook endpoint.

        Args:
            webhook_id: Webhook ID

        Returns:
            Disabled webhook
        """
        return self.http.post(f"{self.base_path}/{webhook_id}/disable")

    def test_webhook(self, webhook_id: str) -> dict:
        """
        Test a webhook endpoint with a sample payload.

        Args:
            webhook_id: Webhook ID

        Returns:
            Test result
        """
        return self.http.post(f"{self.base_path}/{webhook_id}/test")

    # Deliveries
    def list_deliveries(
        self,
        webhook_id: str,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List webhook deliveries.

        Args:
            webhook_id: Webhook ID
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by delivery status

        Returns:
            Paginated list of deliveries
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/{webhook_id}/deliveries", params=params)

    def get_delivery(self, webhook_id: str, delivery_id: str) -> dict:
        """
        Get webhook delivery details.

        Args:
            webhook_id: Webhook ID
            delivery_id: Delivery ID

        Returns:
            Delivery details
        """
        return self.http.get(f"{self.base_path}/{webhook_id}/deliveries/{delivery_id}")

    def retry_delivery(self, webhook_id: str, delivery_id: str) -> dict:
        """
        Retry a failed webhook delivery.

        Args:
            webhook_id: Webhook ID
            delivery_id: Delivery ID

        Returns:
            Retry result
        """
        return self.http.post(
            f"{self.base_path}/{webhook_id}/deliveries/{delivery_id}/retry"
        )

    # Event Types
    def list_event_types(self) -> list:
        """
        List available webhook event types.

        Returns:
            List of event types
        """
        return self.http.get(f"{self.base_path}/event-types")
