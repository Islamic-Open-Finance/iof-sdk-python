"""Events Rail API client."""

from typing import Any, Optional

from ..models import Event, PaginatedResponse


class EventsRail:
    """
    Events Rail API client.

    Handles event publishing and subscription management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Events rail client."""
        self.http = http_client
        self.base_path = "/api/v1/events"

    def list_events(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        source: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List events with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by event type
            source: Filter by source
            start_date: Filter by start date (ISO format)
            end_date: Filter by end date (ISO format)

        Returns:
            Paginated list of events
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "source": source,
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(self.base_path, params=params)

    def get_event(self, event_id: str) -> Event:
        """
        Get event by ID.

        Args:
            event_id: Event ID

        Returns:
            Event details
        """
        return self.http.get(f"{self.base_path}/{event_id}")

    def publish_event(self, data: dict) -> Event:
        """
        Publish a new event.

        Args:
            data: Event data

        Returns:
            Published event
        """
        return self.http.post(self.base_path, json=data)

    # Event Types
    def list_event_types(self) -> list:
        """
        List available event types.

        Returns:
            List of event types
        """
        return self.http.get(f"{self.base_path}/types")

    def get_event_schema(self, event_type: str) -> dict:
        """
        Get event schema for a specific type.

        Args:
            event_type: Event type

        Returns:
            Event schema
        """
        return self.http.get(f"{self.base_path}/types/{event_type}/schema")

    # Subscriptions
    def list_subscriptions(
        self,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List event subscriptions.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of subscriptions
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/subscriptions", params=params)

    def create_subscription(self, data: dict) -> dict:
        """
        Create an event subscription.

        Args:
            data: Subscription data

        Returns:
            Created subscription
        """
        return self.http.post(f"{self.base_path}/subscriptions", json=data)

    def delete_subscription(self, subscription_id: str) -> None:
        """
        Delete an event subscription.

        Args:
            subscription_id: Subscription ID
        """
        self.http.delete(f"{self.base_path}/subscriptions/{subscription_id}")
