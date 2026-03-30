"""Islamic Funds Rail API client."""

from typing import Any, Optional


class FundsRail:
    """Islamic Funds Rail - fund management, subscriptions, performance, and compliance."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/funds"

    # Fund Management
    def list_funds(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Islamic funds."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/management", params=params)

    def get_fund(self, fund_id: str) -> dict:
        """Get fund by ID."""
        return self.http.get(f"{self.base_path}/management/{fund_id}")

    def create_fund(self, data: dict) -> dict:
        """Create a new Islamic fund."""
        return self.http.post(f"{self.base_path}/management", json=data)

    # Subscriptions
    def list_subscriptions(self, fund_id: str, page: int = 1, limit: int = 20) -> dict:
        """List fund subscriptions."""
        params = {"fund_id": fund_id, "page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/subscription", params=params)

    def subscribe(self, data: dict) -> dict:
        """Subscribe to a fund."""
        return self.http.post(f"{self.base_path}/subscription", json=data)

    def redeem(self, subscription_id: str, data: dict) -> dict:
        """Redeem fund units."""
        return self.http.post(f"{self.base_path}/subscription/{subscription_id}/redeem", json=data)

    # Fees
    def calculate_fees(self, fund_id: str, data: dict) -> dict:
        """Calculate fund fees."""
        return self.http.post(f"{self.base_path}/fees/calculate", json={"fund_id": fund_id, **data})

    # Performance
    def get_performance(self, fund_id: str, period: Optional[str] = None) -> dict:
        """Get fund performance metrics."""
        params = {"period": period}
        return self.http.get(f"{self.base_path}/performance/{fund_id}", params=params)

    # Compliance
    def check_compliance(self, fund_id: str) -> dict:
        """Check fund Shariah compliance."""
        return self.http.get(f"{self.base_path}/compliance/{fund_id}")

    # Distribution
    def list_distributions(self, fund_id: str) -> dict:
        """List fund distributions."""
        return self.http.get(f"{self.base_path}/distribution", params={"fund_id": fund_id})

    def create_distribution(self, data: dict) -> dict:
        """Create a fund distribution."""
        return self.http.post(f"{self.base_path}/distribution", json=data)

    # Reporting
    def get_report(self, fund_id: str, report_type: str) -> dict:
        """Get fund report."""
        params = {"report_type": report_type}
        return self.http.get(f"{self.base_path}/reporting/{fund_id}", params=params)
