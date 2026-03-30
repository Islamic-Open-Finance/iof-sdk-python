"""Debt Facilities & Receivables Rail API client."""

from typing import Any, Optional


class DebtRail:
    """Debt Rail - facilities, schedules, covenants, and collections."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/debt"

    # Facilities
    def list_facilities(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List debt facilities."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/facilities", params=params)

    def get_facility(self, facility_id: str) -> dict:
        """Get debt facility by ID."""
        return self.http.get(f"{self.base_path}/facilities/{facility_id}")

    def create_facility(self, data: dict) -> dict:
        """Create a debt facility."""
        return self.http.post(f"{self.base_path}/facilities", json=data)

    # Schedules
    def list_schedules(self, facility_id: str) -> dict:
        """List payment schedules for a facility."""
        return self.http.get(f"{self.base_path}/schedules", params={"facility_id": facility_id})

    def get_schedule(self, schedule_id: str) -> dict:
        """Get payment schedule by ID."""
        return self.http.get(f"{self.base_path}/schedules/{schedule_id}")

    # Covenants
    def list_covenants(self, facility_id: str) -> dict:
        """List covenants for a facility."""
        return self.http.get(f"{self.base_path}/covenants", params={"facility_id": facility_id})

    def check_covenant(self, covenant_id: str) -> dict:
        """Check covenant compliance."""
        return self.http.post(f"{self.base_path}/covenants/{covenant_id}/check")

    # Collections
    def list_collections(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List collection activities."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/collections", params=params)

    def create_collection(self, data: dict) -> dict:
        """Create a collection activity."""
        return self.http.post(f"{self.base_path}/collections", json=data)
