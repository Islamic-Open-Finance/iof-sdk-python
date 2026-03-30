"""Omnichannel Rail API client."""

from typing import Any, Optional


class OmnichannelRail:
    """Omnichannel Rail - cross-channel journeys, approvals, delegations, and templates."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/omni"

    # Journeys
    def list_journeys(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List omnichannel journeys."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/journeys", params=params)

    def get_journey(self, journey_id: str) -> dict:
        """Get journey by ID."""
        return self.http.get(f"{self.base_path}/journeys/{journey_id}")

    def create_journey(self, data: dict) -> dict:
        """Create a new journey."""
        return self.http.post(f"{self.base_path}/journeys", json=data)

    # Templates
    def list_templates(self, page: int = 1, limit: int = 20) -> dict:
        """List journey templates."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/templates", params=params)

    def get_template(self, template_id: str) -> dict:
        """Get template by ID."""
        return self.http.get(f"{self.base_path}/templates/{template_id}")

    # Delegations
    def list_delegations(self, page: int = 1, limit: int = 20) -> dict:
        """List delegations."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/delegations", params=params)

    def create_delegation(self, data: dict) -> dict:
        """Create a delegation."""
        return self.http.post(f"{self.base_path}/delegations", json=data)

    # Approvals
    def list_approvals(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List pending approvals."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/approvals", params=params)

    def approve(self, approval_id: str, data: Optional[dict] = None) -> dict:
        """Approve a request."""
        return self.http.post(f"{self.base_path}/approvals/{approval_id}/approve", json=data or {})

    def reject(self, approval_id: str, reason: str) -> dict:
        """Reject a request."""
        return self.http.post(f"{self.base_path}/approvals/{approval_id}/reject", json={"reason": reason})

    # Timeline
    def get_timeline(self, entity_id: str) -> dict:
        """Get entity timeline."""
        return self.http.get(f"{self.base_path}/timeline/{entity_id}")
