"""Invitations Rail API client."""

from typing import Any, Optional


class InvitationsRail:
    """User and workspace invitations management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/invitations"

    def list_invitations(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List invitations."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_invitation(self, invitation_id: str) -> dict:
        """Get invitation by ID."""
        return self.http.get(f"{self.base_path}/{invitation_id}")

    def create_invitation(self, data: dict) -> dict:
        """Create and send an invitation."""
        return self.http.post(self.base_path, json=data)

    def resend_invitation(self, invitation_id: str) -> dict:
        """Resend an invitation email."""
        return self.http.post(f"{self.base_path}/{invitation_id}/resend")

    def revoke_invitation(self, invitation_id: str) -> dict:
        """Revoke a pending invitation."""
        return self.http.post(f"{self.base_path}/{invitation_id}/revoke")

    def accept_invitation(self, token: str, data: dict) -> dict:
        """Accept an invitation using a token."""
        return self.http.post(f"{self.base_path}/accept", json={"token": token, **data})

    def validate_token(self, token: str) -> dict:
        """Validate an invitation token."""
        params = {"token": token}
        return self.http.get(f"{self.base_path}/validate", params=params)
