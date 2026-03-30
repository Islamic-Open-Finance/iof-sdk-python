"""GDPR Rail API client."""

from typing import Any, Optional


class GDPRRail:
    """GDPR data subject rights and privacy management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/gdpr"

    def list_requests(self, page: int = 1, limit: int = 20, request_type: Optional[str] = None) -> dict:
        """List data subject requests."""
        params = {"page": page, "limit": limit, "request_type": request_type}
        return self.http.get(f"{self.base_path}/requests", params=params)

    def get_request(self, request_id: str) -> dict:
        """Get data subject request by ID."""
        return self.http.get(f"{self.base_path}/requests/{request_id}")

    def submit_access_request(self, data: dict) -> dict:
        """Submit a data access (SAR) request."""
        return self.http.post(f"{self.base_path}/requests/access", json=data)

    def submit_erasure_request(self, data: dict) -> dict:
        """Submit a right-to-erasure request."""
        return self.http.post(f"{self.base_path}/requests/erasure", json=data)

    def submit_portability_request(self, data: dict) -> dict:
        """Submit a data portability request."""
        return self.http.post(f"{self.base_path}/requests/portability", json=data)

    def process_request(self, request_id: str, data: dict) -> dict:
        """Process a data subject request."""
        return self.http.post(f"{self.base_path}/requests/{request_id}/process", json=data)

    def list_consents(self, subject_id: str) -> dict:
        """List consent records for a data subject."""
        return self.http.get(f"{self.base_path}/consents/{subject_id}")

    def get_data_map(self) -> dict:
        """Get the data processing map (Record of Processing Activities)."""
        return self.http.get(f"{self.base_path}/data-map")

    def get_retention_policy(self, data_category: str) -> dict:
        """Get retention policy for a data category."""
        return self.http.get(f"{self.base_path}/retention/{data_category}")
