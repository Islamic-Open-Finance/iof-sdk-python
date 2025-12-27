"""Portfolio Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, Portfolio


class PortfolioRail:
    """
    Portfolio Rail API client.

    Handles investment mandate and portfolio management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Portfolio rail client."""
        self.http = http_client
        self.base_path = "/api/v1/portfolio"

    # Portfolios
    def list_portfolios(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List portfolios.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by portfolio type

        Returns:
            Paginated list of portfolios
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
        }
        return self.http.get(self.base_path, params=params)

    def get_portfolio(self, portfolio_id: str) -> Portfolio:
        """
        Get portfolio by ID.

        Args:
            portfolio_id: Portfolio ID

        Returns:
            Portfolio details
        """
        return self.http.get(f"{self.base_path}/{portfolio_id}")

    def create_portfolio(self, data: dict) -> Portfolio:
        """
        Create a new portfolio.

        Args:
            data: Portfolio creation data

        Returns:
            Created portfolio
        """
        return self.http.post(self.base_path, json=data)

    def update_portfolio(self, portfolio_id: str, data: dict) -> Portfolio:
        """
        Update a portfolio.

        Args:
            portfolio_id: Portfolio ID
            data: Portfolio update data

        Returns:
            Updated portfolio
        """
        return self.http.patch(f"{self.base_path}/{portfolio_id}", json=data)

    # Holdings
    def get_holdings(self, portfolio_id: str) -> list:
        """
        Get portfolio holdings.

        Args:
            portfolio_id: Portfolio ID

        Returns:
            List of holdings
        """
        return self.http.get(f"{self.base_path}/{portfolio_id}/holdings")

    def add_holding(self, portfolio_id: str, data: dict) -> dict:
        """
        Add a holding to portfolio.

        Args:
            portfolio_id: Portfolio ID
            data: Holding data

        Returns:
            Created holding
        """
        return self.http.post(f"{self.base_path}/{portfolio_id}/holdings", json=data)

    # Performance
    def get_performance(
        self,
        portfolio_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get portfolio performance.

        Args:
            portfolio_id: Portfolio ID
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            Performance metrics
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(
            f"{self.base_path}/{portfolio_id}/performance", params=params
        )

    # Mandates
    def get_mandate(self, portfolio_id: str) -> dict:
        """
        Get portfolio investment mandate.

        Args:
            portfolio_id: Portfolio ID

        Returns:
            Investment mandate
        """
        return self.http.get(f"{self.base_path}/{portfolio_id}/mandate")

    def update_mandate(self, portfolio_id: str, data: dict) -> dict:
        """
        Update portfolio investment mandate.

        Args:
            portfolio_id: Portfolio ID
            data: Mandate data

        Returns:
            Updated mandate
        """
        return self.http.put(f"{self.base_path}/{portfolio_id}/mandate", json=data)

    def check_compliance(self, portfolio_id: str) -> dict:
        """
        Check portfolio compliance with mandate.

        Args:
            portfolio_id: Portfolio ID

        Returns:
            Compliance check result
        """
        return self.http.get(f"{self.base_path}/{portfolio_id}/compliance")
