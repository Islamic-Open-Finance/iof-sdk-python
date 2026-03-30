"""Passkeys Rail API client."""

from typing import Any, Optional


class PasskeysRail:
    """WebAuthn / FIDO2 passkey registration and authentication rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/passkeys"

    def list_passkeys(self, page: int = 1, limit: int = 20) -> dict:
        """List registered passkeys for the authenticated user."""
        params = {"page": page, "limit": limit}
        return self.http.get(self.base_path, params=params)

    def get_passkey(self, passkey_id: str) -> dict:
        """Get passkey registration by ID."""
        return self.http.get(f"{self.base_path}/{passkey_id}")

    def begin_registration(self, data: dict) -> dict:
        """Begin passkey registration (returns challenge)."""
        return self.http.post(f"{self.base_path}/registration/begin", json=data)

    def complete_registration(self, data: dict) -> dict:
        """Complete passkey registration with authenticator response."""
        return self.http.post(f"{self.base_path}/registration/complete", json=data)

    def begin_authentication(self, data: dict) -> dict:
        """Begin passkey authentication (returns challenge)."""
        return self.http.post(f"{self.base_path}/authentication/begin", json=data)

    def complete_authentication(self, data: dict) -> dict:
        """Complete passkey authentication with authenticator response."""
        return self.http.post(f"{self.base_path}/authentication/complete", json=data)

    def delete_passkey(self, passkey_id: str) -> dict:
        """Revoke and delete a registered passkey."""
        return self.http.delete(f"{self.base_path}/{passkey_id}")

    def update_passkey(self, passkey_id: str, data: dict) -> dict:
        """Update passkey metadata (e.g. display name)."""
        return self.http.patch(f"{self.base_path}/{passkey_id}", json=data)
