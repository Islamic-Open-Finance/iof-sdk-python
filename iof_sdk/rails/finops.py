"""FinOps Rail API client."""

from typing import Any, Optional


class FinOpsRail:
    """Financial operations and cost management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/finops"

    def get_cost_summary(self, period: Optional[str] = None) -> dict:
        """Get cost summary for the given period."""
        params = {"period": period}
        return self.http.get(f"{self.base_path}/costs", params=params)

    def list_cost_centers(self, page: int = 1, limit: int = 20) -> dict:
        """List cost centers."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/cost-centers", params=params)

    def get_cost_center(self, cost_center_id: str) -> dict:
        """Get cost center by ID."""
        return self.http.get(f"{self.base_path}/cost-centers/{cost_center_id}")

    def create_cost_center(self, data: dict) -> dict:
        """Create a cost center."""
        return self.http.post(f"{self.base_path}/cost-centers", json=data)

    def list_budgets(self, page: int = 1, limit: int = 20) -> dict:
        """List budgets."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/budgets", params=params)

    def get_budget(self, budget_id: str) -> dict:
        """Get budget by ID."""
        return self.http.get(f"{self.base_path}/budgets/{budget_id}")

    def create_budget(self, data: dict) -> dict:
        """Create a budget."""
        return self.http.post(f"{self.base_path}/budgets", json=data)

    def get_forecast(self, data: dict) -> dict:
        """Get cost forecast."""
        return self.http.post(f"{self.base_path}/forecast", json=data)

    def list_allocations(self, page: int = 1, limit: int = 20) -> dict:
        """List cost allocations."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/allocations", params=params)
