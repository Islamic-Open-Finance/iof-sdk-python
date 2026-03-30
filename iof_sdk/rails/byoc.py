"""BYOC (Bring Your Own Cloud) Rail API client."""

from typing import Any, Optional


class BYOCRail:
    """Bring Your Own Cloud deployment and configuration rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/byoc"

    def list_deployments(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List BYOC deployments."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_deployment(self, deployment_id: str) -> dict:
        """Get BYOC deployment by ID."""
        return self.http.get(f"{self.base_path}/{deployment_id}")

    def create_deployment(self, data: dict) -> dict:
        """Create a new BYOC deployment."""
        return self.http.post(self.base_path, json=data)

    def update_deployment(self, deployment_id: str, data: dict) -> dict:
        """Update a BYOC deployment configuration."""
        return self.http.patch(f"{self.base_path}/{deployment_id}", json=data)

    def delete_deployment(self, deployment_id: str) -> dict:
        """Delete a BYOC deployment."""
        return self.http.delete(f"{self.base_path}/{deployment_id}")

    def get_health(self, deployment_id: str) -> dict:
        """Get health status of a BYOC deployment."""
        return self.http.get(f"{self.base_path}/{deployment_id}/health")

    def list_regions(self) -> dict:
        """List available BYOC deployment regions."""
        return self.http.get(f"{self.base_path}/regions")

    def get_manifest(self, deployment_id: str) -> dict:
        """Get deployment manifest (Helm chart / docker-compose)."""
        return self.http.get(f"{self.base_path}/{deployment_id}/manifest")

    def rotate_credentials(self, deployment_id: str) -> dict:
        """Rotate deployment credentials."""
        return self.http.post(f"{self.base_path}/{deployment_id}/rotate-credentials")
