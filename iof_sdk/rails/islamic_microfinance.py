"""Islamic Microfinance Rail API client."""

from typing import Any, Optional


class IslamicMicrofinanceRail:
    """Islamic microfinance products and portfolio management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/islamic-microfinance"

    def list_loans(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List microfinance loans."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_loan(self, loan_id: str) -> dict:
        """Get microfinance loan by ID."""
        return self.http.get(f"{self.base_path}/{loan_id}")

    def create_loan(self, data: dict) -> dict:
        """Create a microfinance loan application."""
        return self.http.post(self.base_path, json=data)

    def approve_loan(self, loan_id: str, data: dict) -> dict:
        """Approve a microfinance loan."""
        return self.http.post(f"{self.base_path}/{loan_id}/approve", json=data)

    def disburse_loan(self, loan_id: str, data: dict) -> dict:
        """Disburse a microfinance loan."""
        return self.http.post(f"{self.base_path}/{loan_id}/disburse", json=data)

    def list_repayments(self, loan_id: str, page: int = 1, limit: int = 20) -> dict:
        """List repayment schedule for a loan."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/{loan_id}/repayments", params=params)

    def record_repayment(self, loan_id: str, data: dict) -> dict:
        """Record a repayment for a loan."""
        return self.http.post(f"{self.base_path}/{loan_id}/repayments", json=data)

    def get_group(self, group_id: str) -> dict:
        """Get a solidarity/lending group."""
        return self.http.get(f"{self.base_path}/groups/{group_id}")

    def list_groups(self, page: int = 1, limit: int = 20) -> dict:
        """List solidarity/lending groups."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/groups", params=params)

    def create_group(self, data: dict) -> dict:
        """Create a solidarity/lending group."""
        return self.http.post(f"{self.base_path}/groups", json=data)
