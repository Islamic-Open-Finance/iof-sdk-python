"""Ujrah (Fee-Based Service) Rail API client."""

from typing import Any, Optional


class UjrahRail:
    """Ujrah (Fee-Based Service) Rail API client."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/ujrah"

    def list_contracts(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Ujrah (Fee-Based Service) contracts."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_contract(self, contract_id: str) -> dict:
        """Get Ujrah (Fee-Based Service) contract by ID."""
        return self.http.get(f"{self.base_path}/{contract_id}")

    def create_contract(self, data: dict) -> dict:
        """Create a new Ujrah (Fee-Based Service) contract."""
        return self.http.post(self.base_path, json=data)

    def update_contract(self, contract_id: str, data: dict) -> dict:
        """Update a Ujrah (Fee-Based Service) contract."""
        return self.http.patch(f"{self.base_path}/{contract_id}", json=data)

    def execute_contract(self, contract_id: str) -> dict:
        """Execute a Ujrah (Fee-Based Service) contract."""
        return self.http.post(f"{self.base_path}/{contract_id}/execute")

    def validate(self, data: dict) -> dict:
        """Validate Ujrah (Fee-Based Service) contract data."""
        return self.http.post(f"{self.base_path}/validate", json=data)
