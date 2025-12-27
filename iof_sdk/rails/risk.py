"""Risk Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, RiskLimit


class RiskRail:
    """
    Risk Rail API client.

    Handles exposure and limit management for risk control.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Risk rail client."""
        self.http = http_client
        self.base_path = "/api/v1/risk"

    # Limits
    def list_limits(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List risk limits.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by limit type
            status: Filter by status

        Returns:
            Paginated list of risk limits
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/limits", params=params)

    def get_limit(self, limit_id: str) -> RiskLimit:
        """
        Get risk limit by ID.

        Args:
            limit_id: Limit ID

        Returns:
            Risk limit details
        """
        return self.http.get(f"{self.base_path}/limits/{limit_id}")

    def create_limit(self, data: dict) -> RiskLimit:
        """
        Create a new risk limit.

        Args:
            data: Limit creation data

        Returns:
            Created risk limit
        """
        return self.http.post(f"{self.base_path}/limits", json=data)

    def update_limit(self, limit_id: str, data: dict) -> RiskLimit:
        """
        Update a risk limit.

        Args:
            limit_id: Limit ID
            data: Limit update data

        Returns:
            Updated risk limit
        """
        return self.http.patch(f"{self.base_path}/limits/{limit_id}", json=data)

    def check_limit(self, limit_id: str, amount: float) -> dict:
        """
        Check if an amount would breach a limit.

        Args:
            limit_id: Limit ID
            amount: Amount to check

        Returns:
            Limit check result
        """
        return self.http.post(
            f"{self.base_path}/limits/{limit_id}/check", json={"amount": amount}
        )

    # Exposure
    def get_exposure_summary(
        self,
        entity_id: Optional[str] = None,
        currency: Optional[str] = None,
    ) -> dict:
        """
        Get exposure summary.

        Args:
            entity_id: Entity ID (optional)
            currency: Currency filter (optional)

        Returns:
            Exposure summary
        """
        params = {
            "entity_id": entity_id,
            "currency": currency,
        }
        return self.http.get(f"{self.base_path}/exposure", params=params)

    def get_concentration_risk(self) -> dict:
        """
        Get concentration risk analysis.

        Returns:
            Concentration risk report
        """
        return self.http.get(f"{self.base_path}/concentration")

    # Assessments
    def create_risk_assessment(self, data: dict) -> dict:
        """
        Create a risk assessment.

        Args:
            data: Assessment data

        Returns:
            Created risk assessment
        """
        return self.http.post(f"{self.base_path}/assessments", json=data)

    def list_assessments(
        self,
        page: int = 1,
        limit: int = 20,
    ) -> PaginatedResponse:
        """
        List risk assessments.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of assessments
        """
        params = {
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/assessments", params=params)
