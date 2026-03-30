"""Takaful (Islamic Insurance) Rail API client."""

from typing import Any, Optional


class TakafulRail:
    """Takaful Rail - Islamic insurance products, claims, underwriting, and compliance."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/takaful"

    # General Takaful
    def list_policies(self, page: int = 1, limit: int = 20, type: Optional[str] = None, status: Optional[str] = None) -> dict:
        """List Takaful policies."""
        params = {"page": page, "limit": limit, "type": type, "status": status}
        return self.http.get(f"{self.base_path}/general", params=params)

    def get_policy(self, policy_id: str) -> dict:
        """Get Takaful policy by ID."""
        return self.http.get(f"{self.base_path}/general/{policy_id}")

    def create_policy(self, data: dict) -> dict:
        """Create a Takaful policy."""
        return self.http.post(f"{self.base_path}/general", json=data)

    # Family Takaful
    def list_family_plans(self, page: int = 1, limit: int = 20) -> dict:
        """List Family Takaful plans."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/family", params=params)

    def create_family_plan(self, data: dict) -> dict:
        """Create a Family Takaful plan."""
        return self.http.post(f"{self.base_path}/family", json=data)

    # Claims
    def list_claims(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Takaful claims."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/claims", params=params)

    def get_claim(self, claim_id: str) -> dict:
        """Get claim by ID."""
        return self.http.get(f"{self.base_path}/claims/{claim_id}")

    def submit_claim(self, data: dict) -> dict:
        """Submit a new claim."""
        return self.http.post(f"{self.base_path}/claims", json=data)

    # Underwriting
    def submit_underwriting(self, data: dict) -> dict:
        """Submit for underwriting."""
        return self.http.post(f"{self.base_path}/underwriting", json=data)

    # Reinsurance (Retakaful)
    def list_reinsurance(self, page: int = 1, limit: int = 20) -> dict:
        """List retakaful arrangements."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/reinsurance", params=params)

    # Fund Management
    def get_fund_status(self) -> dict:
        """Get Takaful fund status."""
        return self.http.get(f"{self.base_path}/fund-management")

    # Surplus Distribution
    def calculate_surplus(self, period: str) -> dict:
        """Calculate surplus distribution."""
        return self.http.post(f"{self.base_path}/surplus/calculate", json={"period": period})

    # Compliance
    def check_compliance(self, policy_id: str) -> dict:
        """Check policy Shariah compliance."""
        return self.http.get(f"{self.base_path}/compliance/{policy_id}")

    # Actuarial
    def get_actuarial_report(self, report_id: str) -> dict:
        """Get actuarial report."""
        return self.http.get(f"{self.base_path}/actuarial/{report_id}")
