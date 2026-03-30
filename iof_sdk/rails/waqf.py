"""Waqf & Social Finance Rail API client."""

from typing import Any, Optional


class WaqfRail:
    """Waqf Rail - endowment management, Waqf Sukuk, Sadaqah, and Qard Hasan."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/waqf"

    # Waqf Management
    def list_waqf(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Waqf endowments."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/management", params=params)

    def get_waqf(self, waqf_id: str) -> dict:
        """Get Waqf endowment by ID."""
        return self.http.get(f"{self.base_path}/management/{waqf_id}")

    def create_waqf(self, data: dict) -> dict:
        """Create a new Waqf endowment."""
        return self.http.post(f"{self.base_path}/management", json=data)

    def update_waqf(self, waqf_id: str, data: dict) -> dict:
        """Update a Waqf endowment."""
        return self.http.patch(f"{self.base_path}/management/{waqf_id}", json=data)

    # Waqf Sukuk
    def list_waqf_sukuk(self, page: int = 1, limit: int = 20) -> dict:
        """List Waqf Sukuk instruments."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/sukuk", params=params)

    def create_waqf_sukuk(self, data: dict) -> dict:
        """Create a Waqf Sukuk issuance."""
        return self.http.post(f"{self.base_path}/sukuk", json=data)


class SadaqahRail:
    """Sadaqah Rail - voluntary charity management."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/sadaqah"

    def list_donations(self, page: int = 1, limit: int = 20) -> dict:
        """List Sadaqah donations."""
        params = {"page": page, "limit": limit}
        return self.http.get(self.base_path, params=params)

    def create_donation(self, data: dict) -> dict:
        """Record a Sadaqah donation."""
        return self.http.post(self.base_path, json=data)

    def get_donation(self, donation_id: str) -> dict:
        """Get donation by ID."""
        return self.http.get(f"{self.base_path}/{donation_id}")


class QardHasanRail:
    """Qard Hasan Rail - interest-free benevolent loans."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/qard-hasan"

    def list_loans(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Qard Hasan loans."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_loan(self, loan_id: str) -> dict:
        """Get loan by ID."""
        return self.http.get(f"{self.base_path}/{loan_id}")

    def create_loan(self, data: dict) -> dict:
        """Create a Qard Hasan loan."""
        return self.http.post(self.base_path, json=data)

    def record_repayment(self, loan_id: str, data: dict) -> dict:
        """Record a loan repayment."""
        return self.http.post(f"{self.base_path}/{loan_id}/repayment", json=data)
