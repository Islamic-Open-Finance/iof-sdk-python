"""Residency Rail API client."""

from typing import Any, Optional


class ResidencyRail:
    """Customer residency verification and tax domicile management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/residency"

    def list_records(self, page: int = 1, limit: int = 20, country: Optional[str] = None) -> dict:
        """List residency records."""
        params = {"page": page, "limit": limit, "country": country}
        return self.http.get(self.base_path, params=params)

    def get_record(self, record_id: str) -> dict:
        """Get residency record by ID."""
        return self.http.get(f"{self.base_path}/{record_id}")

    def create_record(self, data: dict) -> dict:
        """Create a residency record."""
        return self.http.post(self.base_path, json=data)

    def update_record(self, record_id: str, data: dict) -> dict:
        """Update a residency record."""
        return self.http.patch(f"{self.base_path}/{record_id}", json=data)

    def verify_residency(self, record_id: str, data: dict) -> dict:
        """Submit residency verification documents."""
        return self.http.post(f"{self.base_path}/{record_id}/verify", json=data)

    def get_tax_domicile(self, customer_id: str) -> dict:
        """Get tax domicile information for a customer."""
        return self.http.get(f"{self.base_path}/tax-domicile/{customer_id}")

    def update_tax_domicile(self, customer_id: str, data: dict) -> dict:
        """Update tax domicile information for a customer."""
        return self.http.patch(f"{self.base_path}/tax-domicile/{customer_id}", json=data)

    def list_jurisdictions(self) -> dict:
        """List supported residency jurisdictions."""
        return self.http.get(f"{self.base_path}/jurisdictions")
