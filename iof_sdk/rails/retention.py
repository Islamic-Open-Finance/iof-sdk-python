"""Retention Rail API client."""

from typing import Any, Optional


class RetentionRail:
    """Data retention policies and lifecycle management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/retention"

    def list_policies(self, page: int = 1, limit: int = 20, data_category: Optional[str] = None) -> dict:
        """List retention policies."""
        params = {"page": page, "limit": limit, "data_category": data_category}
        return self.http.get(self.base_path, params=params)

    def get_policy(self, policy_id: str) -> dict:
        """Get retention policy by ID."""
        return self.http.get(f"{self.base_path}/{policy_id}")

    def create_policy(self, data: dict) -> dict:
        """Create a retention policy."""
        return self.http.post(self.base_path, json=data)

    def update_policy(self, policy_id: str, data: dict) -> dict:
        """Update a retention policy."""
        return self.http.patch(f"{self.base_path}/{policy_id}", json=data)

    def delete_policy(self, policy_id: str) -> dict:
        """Delete a retention policy."""
        return self.http.delete(f"{self.base_path}/{policy_id}")

    def run_purge(self, data: dict) -> dict:
        """Trigger a data purge run based on retention policies."""
        return self.http.post(f"{self.base_path}/purge", json=data)

    def list_purge_runs(self, page: int = 1, limit: int = 20) -> dict:
        """List historical purge runs."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/purge/runs", params=params)

    def get_purge_run(self, run_id: str) -> dict:
        """Get details of a purge run."""
        return self.http.get(f"{self.base_path}/purge/runs/{run_id}")

    def get_retention_schedule(self, data_category: str) -> dict:
        """Get the retention schedule for a specific data category."""
        return self.http.get(f"{self.base_path}/schedule/{data_category}")
