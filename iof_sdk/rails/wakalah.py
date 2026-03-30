"""Wakalah (Agency) Rail API client."""

from typing import Any, Optional


class WakalahRail:
    """Wakalah (Agency) Rail API client."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/wakalah"

    def list_contracts(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Wakalah (Agency) contracts."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_contract(self, contract_id: str) -> dict:
        """Get Wakalah (Agency) contract by ID."""
        return self.http.get(f"{self.base_path}/{contract_id}")

    def create_contract(self, data: dict) -> dict:
        """Create a new Wakalah (Agency) contract."""
        return self.http.post(self.base_path, json=data)

    def update_contract(self, contract_id: str, data: dict) -> dict:
        """Update a Wakalah (Agency) contract."""
        return self.http.patch(f"{self.base_path}/{contract_id}", json=data)

    def execute_contract(self, contract_id: str) -> dict:
        """Execute a Wakalah (Agency) contract."""
        return self.http.post(f"{self.base_path}/{contract_id}/execute")

    def validate(self, data: dict) -> dict:
        """Validate Wakalah (Agency) contract data."""
        return self.http.post(f"{self.base_path}/validate", json=data)
