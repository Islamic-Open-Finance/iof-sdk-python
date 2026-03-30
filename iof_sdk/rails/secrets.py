"""Secrets Rail API client."""

from typing import Any, Optional


class SecretsRail:
    """Secrets and credential vault management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/secrets"

    def list_secrets(self, page: int = 1, limit: int = 20, scope: Optional[str] = None) -> dict:
        """List secret metadata (names and scopes, never values)."""
        params = {"page": page, "limit": limit, "scope": scope}
        return self.http.get(self.base_path, params=params)

    def get_secret(self, secret_id: str) -> dict:
        """Get secret metadata by ID (value not returned)."""
        return self.http.get(f"{self.base_path}/{secret_id}")

    def create_secret(self, data: dict) -> dict:
        """Create a new secret."""
        return self.http.post(self.base_path, json=data)

    def update_secret(self, secret_id: str, data: dict) -> dict:
        """Update a secret value or metadata."""
        return self.http.patch(f"{self.base_path}/{secret_id}", json=data)

    def delete_secret(self, secret_id: str) -> dict:
        """Delete a secret permanently."""
        return self.http.delete(f"{self.base_path}/{secret_id}")

    def rotate_secret(self, secret_id: str, data: dict) -> dict:
        """Rotate a secret to a new value."""
        return self.http.post(f"{self.base_path}/{secret_id}/rotate", json=data)

    def list_versions(self, secret_id: str) -> dict:
        """List version history for a secret."""
        return self.http.get(f"{self.base_path}/{secret_id}/versions")

    def get_version(self, secret_id: str, version_id: str) -> dict:
        """Get a specific version of a secret."""
        return self.http.get(f"{self.base_path}/{secret_id}/versions/{version_id}")
