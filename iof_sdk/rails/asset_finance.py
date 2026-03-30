"""Asset Finance Rail API client."""

from typing import Any, Optional


class AssetFinanceRail:
    """Asset finance and Ijarah-based financing rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/asset-finance"

    def list_facilities(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List asset finance facilities."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_facility(self, facility_id: str) -> dict:
        """Get asset finance facility by ID."""
        return self.http.get(f"{self.base_path}/{facility_id}")

    def create_facility(self, data: dict) -> dict:
        """Create an asset finance facility."""
        return self.http.post(self.base_path, json=data)

    def update_facility(self, facility_id: str, data: dict) -> dict:
        """Update an asset finance facility."""
        return self.http.patch(f"{self.base_path}/{facility_id}", json=data)

    def list_assets(self, facility_id: str) -> dict:
        """List assets linked to a facility."""
        return self.http.get(f"{self.base_path}/{facility_id}/assets")

    def add_asset(self, facility_id: str, data: dict) -> dict:
        """Add an asset to a facility."""
        return self.http.post(f"{self.base_path}/{facility_id}/assets", json=data)

    def list_repayments(self, facility_id: str, page: int = 1, limit: int = 20) -> dict:
        """List repayment schedule for a facility."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/{facility_id}/repayments", params=params)

    def process_repayment(self, facility_id: str, data: dict) -> dict:
        """Process a repayment for a facility."""
        return self.http.post(f"{self.base_path}/{facility_id}/repayments", json=data)

    def get_valuation(self, facility_id: str) -> dict:
        """Get current asset valuation for a facility."""
        return self.http.get(f"{self.base_path}/{facility_id}/valuation")
