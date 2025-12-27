"""Developer & Integration Rail API client."""

from typing import Any, Optional

from ..models import ApiKey, DeveloperClient, PaginatedResponse


class DeveloperRail:
    """
    Developer & Integration Rail API client.

    Handles developer portal, API keys, OAuth clients,
    and integration management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Developer rail client."""
        self.http = http_client
        self.base_path = "/api/v1/developer"

    # OAuth Clients
    def list_clients(
        self,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List OAuth/API clients.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of clients
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/clients", params=params)

    def get_client(self, client_id: str) -> DeveloperClient:
        """
        Get OAuth/API client by ID.

        Args:
            client_id: Client ID

        Returns:
            Client details
        """
        return self.http.get(f"{self.base_path}/clients/{client_id}")

    def create_client(self, data: dict) -> DeveloperClient:
        """
        Create a new OAuth/API client.

        Args:
            data: Client creation data

        Returns:
            Created client
        """
        return self.http.post(f"{self.base_path}/clients", json=data)

    def update_client(self, client_id: str, data: dict) -> DeveloperClient:
        """
        Update an OAuth/API client.

        Args:
            client_id: Client ID
            data: Client update data

        Returns:
            Updated client
        """
        return self.http.patch(f"{self.base_path}/clients/{client_id}", json=data)

    def delete_client(self, client_id: str) -> None:
        """
        Delete an OAuth/API client.

        Args:
            client_id: Client ID
        """
        self.http.delete(f"{self.base_path}/clients/{client_id}")

    def rotate_client_secret(self, client_id: str) -> DeveloperClient:
        """
        Rotate OAuth client secret.

        Args:
            client_id: Client ID

        Returns:
            Client with new secret
        """
        return self.http.post(f"{self.base_path}/clients/{client_id}/rotate-secret")

    # API Keys
    def list_api_keys(
        self,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List API keys.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of API keys
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/api-keys", params=params)

    def get_api_key(self, key_id: str) -> ApiKey:
        """
        Get API key by ID.

        Args:
            key_id: API key ID

        Returns:
            API key details
        """
        return self.http.get(f"{self.base_path}/api-keys/{key_id}")

    def create_api_key(self, data: dict) -> ApiKey:
        """
        Create a new API key.

        Args:
            data: API key creation data (name, scopes, expires_at)

        Returns:
            Created API key (includes the actual key value)
        """
        return self.http.post(f"{self.base_path}/api-keys", json=data)

    def delete_api_key(self, key_id: str) -> None:
        """
        Delete an API key.

        Args:
            key_id: API key ID
        """
        self.http.delete(f"{self.base_path}/api-keys/{key_id}")

    def rotate_api_key(self, key_id: str) -> ApiKey:
        """
        Rotate an API key (delete and create new).

        Args:
            key_id: API key ID

        Returns:
            New API key
        """
        return self.http.post(f"{self.base_path}/api-keys/{key_id}/rotate")

    # Webhooks
    def list_webhooks(
        self,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List webhook endpoints.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of webhooks
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/webhooks", params=params)

    def create_webhook(self, data: dict) -> dict:
        """
        Create a new webhook endpoint.

        Args:
            data: Webhook data (url, events, secret)

        Returns:
            Created webhook
        """
        return self.http.post(f"{self.base_path}/webhooks", json=data)

    # Usage & Metrics
    def get_usage_metrics(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get API usage metrics.

        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            Usage metrics
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(f"{self.base_path}/usage", params=params)
