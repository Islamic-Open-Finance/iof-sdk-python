"""Notification Preferences Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class NotificationPreferencesRail:
    """
    Notification Preferences Rail API client.

    Provides notification preference management:
    - User notification profiles
    - Channel preferences
    - Event-level opt-in/opt-out
    - Webhook subscriptions
    - Digest configuration
    - Delivery tracking
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Notification Preferences rail client."""
        self.http = http_client
        self.base_path = "/api/v1/notification-preferences"

    # Profiles

    def create_profile(self, data: dict) -> dict:
        """
        Create a notification profile.

        Args:
            data: Profile data (userId, channels, deliveryWindow, timezone, etc.)

        Returns:
            Created notification profile
        """
        return self.http.post(f"{self.base_path}/profiles", json=data)

    def get_profile(self, profile_id: str) -> dict:
        """
        Get notification profile by ID.

        Args:
            profile_id: Profile ID

        Returns:
            Notification profile details
        """
        return self.http.get(f"{self.base_path}/profiles/{profile_id}")

    def get_profile_by_user_id(self, user_id: str) -> dict:
        """
        Get notification profile by user ID.

        Args:
            user_id: User ID

        Returns:
            Notification profile details
        """
        return self.http.get(
            f"{self.base_path}/profiles/by-user", params={"userId": user_id}
        )

    def update_profile(self, profile_id: str, data: dict) -> dict:
        """
        Update a notification profile.

        Args:
            profile_id: Profile ID
            data: Update data

        Returns:
            Updated notification profile
        """
        return self.http.patch(
            f"{self.base_path}/profiles/{profile_id}", json=data
        )

    def delete_profile(self, profile_id: str) -> None:
        """
        Delete a notification profile.

        Args:
            profile_id: Profile ID
        """
        self.http.delete(f"{self.base_path}/profiles/{profile_id}")

    # Channels

    def update_channel(self, profile_id: str, data: dict) -> dict:
        """
        Update a channel configuration.

        Args:
            profile_id: Profile ID
            data: Channel data (channel, enabled, address)

        Returns:
            Updated notification profile
        """
        channel = data.get("channel", "")
        return self.http.patch(
            f"{self.base_path}/profiles/{profile_id}/channels/{channel}",
            json=data,
        )

    def remove_channel(self, profile_id: str, channel: str) -> dict:
        """
        Remove a channel from a profile.

        Args:
            profile_id: Profile ID
            channel: Channel name

        Returns:
            Updated notification profile
        """
        return self.http.delete(
            f"{self.base_path}/profiles/{profile_id}/channels/{channel}"
        )

    def verify_channel(
        self, profile_id: str, channel: str, code: str
    ) -> dict:
        """
        Verify a channel with a verification code.

        Args:
            profile_id: Profile ID
            channel: Channel name
            code: Verification code

        Returns:
            Updated notification profile
        """
        return self.http.post(
            f"{self.base_path}/profiles/{profile_id}/channels/{channel}/verify",
            json={"code": code},
        )

    def send_verification_code(self, profile_id: str, channel: str) -> None:
        """
        Send a verification code to a channel.

        Args:
            profile_id: Profile ID
            channel: Channel name
        """
        self.http.post(
            f"{self.base_path}/profiles/{profile_id}/channels/{channel}/send-verification"
        )

    # Preferences

    def set_event_preference(self, profile_id: str, data: dict) -> dict:
        """
        Set event-level notification preferences.

        Args:
            profile_id: Profile ID
            data: Event preference data (eventType, enabled, channels, frequency)

        Returns:
            Updated notification profile
        """
        event_type = data.get("eventType", "")
        return self.http.patch(
            f"{self.base_path}/profiles/{profile_id}/events/{event_type}",
            json=data,
        )

    def set_category_preference(self, profile_id: str, data: dict) -> dict:
        """
        Set category-level notification preferences.

        Args:
            profile_id: Profile ID
            data: Category preference data (category, enabled, channels, frequency)

        Returns:
            Updated notification profile
        """
        category = data.get("category", "")
        return self.http.patch(
            f"{self.base_path}/profiles/{profile_id}/categories/{category}",
            json=data,
        )

    # Opt-out

    def global_opt_out(
        self, profile_id: str, reason: Optional[str] = None
    ) -> dict:
        """
        Opt out of all notifications globally.

        Args:
            profile_id: Profile ID
            reason: Optional reason

        Returns:
            Updated notification profile
        """
        data = {}
        if reason:
            data["reason"] = reason
        return self.http.post(
            f"{self.base_path}/profiles/{profile_id}/opt-out", json=data
        )

    def global_opt_in(self, profile_id: str) -> dict:
        """
        Opt back into notifications globally.

        Args:
            profile_id: Profile ID

        Returns:
            Updated notification profile
        """
        return self.http.post(
            f"{self.base_path}/profiles/{profile_id}/opt-in"
        )

    def opt_out(self, profile_id: str, data: dict) -> dict:
        """
        Opt out of specific notifications.

        Args:
            profile_id: Profile ID
            data: Opt-out data (scope, category, eventType, channel, reason)

        Returns:
            Opt-out record
        """
        return self.http.post(
            f"{self.base_path}/profiles/{profile_id}/opt-outs", json=data
        )

    def get_opt_outs(self, profile_id: str) -> dict:
        """
        Get opt-out records for a profile.

        Args:
            profile_id: Profile ID

        Returns:
            List of opt-out records
        """
        return self.http.get(
            f"{self.base_path}/profiles/{profile_id}/opt-outs"
        )

    def remove_opt_out(self, profile_id: str, opt_out_id: str) -> None:
        """
        Remove an opt-out record.

        Args:
            profile_id: Profile ID
            opt_out_id: Opt-out record ID
        """
        self.http.delete(
            f"{self.base_path}/profiles/{profile_id}/opt-outs/{opt_out_id}"
        )

    # Subscriptions

    def list_subscriptions(self) -> dict:
        """
        List webhook subscriptions.

        Returns:
            List of subscriptions
        """
        return self.http.get(f"{self.base_path}/subscriptions")

    def create_subscription(self, data: dict) -> dict:
        """
        Create a webhook subscription.

        Args:
            data: Subscription data (name, channel, endpoint, eventTypes, etc.)

        Returns:
            Created subscription
        """
        return self.http.post(f"{self.base_path}/subscriptions", json=data)

    def get_subscription(self, subscription_id: str) -> dict:
        """
        Get subscription by ID.

        Args:
            subscription_id: Subscription ID

        Returns:
            Subscription details
        """
        return self.http.get(
            f"{self.base_path}/subscriptions/{subscription_id}"
        )

    def update_subscription(self, subscription_id: str, data: dict) -> dict:
        """
        Update a subscription.

        Args:
            subscription_id: Subscription ID
            data: Update data

        Returns:
            Updated subscription
        """
        return self.http.patch(
            f"{self.base_path}/subscriptions/{subscription_id}", json=data
        )

    def delete_subscription(self, subscription_id: str) -> None:
        """
        Delete a subscription.

        Args:
            subscription_id: Subscription ID
        """
        self.http.delete(
            f"{self.base_path}/subscriptions/{subscription_id}"
        )

    def pause_subscription(self, subscription_id: str) -> dict:
        """
        Pause a subscription.

        Args:
            subscription_id: Subscription ID

        Returns:
            Updated subscription
        """
        return self.http.post(
            f"{self.base_path}/subscriptions/{subscription_id}/pause"
        )

    def resume_subscription(self, subscription_id: str) -> dict:
        """
        Resume a paused subscription.

        Args:
            subscription_id: Subscription ID

        Returns:
            Updated subscription
        """
        return self.http.post(
            f"{self.base_path}/subscriptions/{subscription_id}/resume"
        )

    def test_subscription(self, subscription_id: str) -> dict:
        """
        Test a subscription delivery.

        Args:
            subscription_id: Subscription ID

        Returns:
            Test result (success, error)
        """
        return self.http.post(
            f"{self.base_path}/subscriptions/{subscription_id}/test"
        )

    # Digest

    def configure_digest(self, profile_id: str, data: dict) -> dict:
        """
        Configure digest notifications.

        Args:
            profile_id: Profile ID
            data: Digest config (frequency, hour, timezone, categories, channel)

        Returns:
            Digest configuration
        """
        return self.http.patch(
            f"{self.base_path}/profiles/{profile_id}/digest", json=data
        )

    def get_digest_config(self, profile_id: str) -> dict:
        """
        Get digest configuration.

        Args:
            profile_id: Profile ID

        Returns:
            Digest configuration or None
        """
        return self.http.get(
            f"{self.base_path}/profiles/{profile_id}/digest"
        )

    def disable_digest(self, profile_id: str) -> None:
        """
        Disable digest notifications.

        Args:
            profile_id: Profile ID
        """
        self.http.delete(f"{self.base_path}/profiles/{profile_id}/digest")

    # Deliveries

    def list_deliveries(
        self,
        page: int = 1,
        limit: int = 20,
        profile_id: Optional[str] = None,
        status: Optional[str] = None,
        channel: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List notification deliveries.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            profile_id: Filter by profile ID
            status: Filter by delivery status
            channel: Filter by channel

        Returns:
            Paginated list of deliveries
        """
        params = {
            "page": page,
            "limit": limit,
            "profileId": profile_id,
            "status": status,
            "channel": channel,
        }
        return self.http.get(f"{self.base_path}/deliveries", params=params)

    def get_delivery(self, delivery_id: str) -> dict:
        """
        Get delivery by ID.

        Args:
            delivery_id: Delivery ID

        Returns:
            Delivery details
        """
        return self.http.get(f"{self.base_path}/deliveries/{delivery_id}")

    # Utilities

    def should_send_notification(
        self,
        user_id: str,
        event_type: str,
        category: str,
        channel: str,
    ) -> dict:
        """
        Check if a notification should be sent.

        Args:
            user_id: User ID
            event_type: Event type
            category: Event category
            channel: Notification channel

        Returns:
            Check result (shouldSend, reason)
        """
        return self.http.post(
            f"{self.base_path}/check",
            json={
                "userId": user_id,
                "eventType": event_type,
                "category": category,
                "channel": channel,
            },
        )

    def get_available_event_types(self) -> dict:
        """
        Get available notification event types.

        Returns:
            List of event types with categories and defaults
        """
        return self.http.get(f"{self.base_path}/event-types")
