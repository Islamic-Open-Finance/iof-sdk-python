"""API Keys Rail API client."""

from typing import Any, List, Optional

from ..models import PaginatedResponse


class ApiKeysRail:
    """
    API Keys Rail API client.

    Provides API key management capabilities:
    - Create and manage API keys
    - List and filter API keys
    - Revoke and rotate keys
    - Permission and scope management
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the API Keys rail client."""
        self.http = http_client
        self.base_path = "/api/v1/api-keys"

    def list_api_keys(
        self,
        page: int = 1,
        limit: int = 20,
        workspace_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List API keys with filtering and pagination.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            workspace_id: Filter by workspace ID
            status: Filter by status (ACTIVE, REVOKED, EXPIRED)

        Returns:
            Paginated list of API keys
        """
        params = {
            "page": page,
            "limit": limit,
            "workspaceId": workspace_id,
            "status": status,
        }
        return self.http.get(self.base_path, params=params)

    def get_api_key(self, key_id: str) -> dict:
        """
        Get API key by ID.

        Args:
            key_id: API key ID

        Returns:
            API key details
        """
        return self.http.get(f"{self.base_path}/{key_id}")

    def create_api_key(self, data: dict) -> dict:
        """
        Create a new API key.

        Note: The plaintext key is only returned once at creation. Save it securely.

        Args:
            data: API key creation data (name, scopes, permissions, expiresAt)

        Returns:
            Created API key with plaintext key
        """
        return self.http.post(self.base_path, json=data)

    def update_api_key(self, key_id: str, data: dict) -> dict:
        """
        Update API key metadata and permissions.

        Args:
            key_id: API key ID
            data: Update data (name, description, scopes, permissions)

        Returns:
            Updated API key
        """
        return self.http.patch(f"{self.base_path}/{key_id}", json=data)

    def revoke_api_key(self, key_id: str) -> dict:
        """
        Revoke an API key (soft delete).

        Args:
            key_id: API key ID

        Returns:
            Revocation confirmation
        """
        return self.http.post(f"{self.base_path}/{key_id}/revoke")

    def delete_api_key(self, key_id: str) -> dict:
        """
        Delete an API key permanently.

        Args:
            key_id: API key ID

        Returns:
            Deletion confirmation
        """
        return self.http.delete(f"{self.base_path}/{key_id}")

    def rotate_api_key(self, key_id: str) -> dict:
        """
        Rotate an API key (revoke old, create new).

        Note: The new plaintext key is only returned once. Save it securely.

        Args:
            key_id: API key ID

        Returns:
            New API key with plaintext key
        """
        return self.http.post(f"{self.base_path}/{key_id}/rotate")
