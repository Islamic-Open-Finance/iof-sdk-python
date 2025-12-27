"""Treasury Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, TreasuryPosition


class TreasuryRail:
    """
    Treasury Rail API client.

    Handles liquidity and cash management operations.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Treasury rail client."""
        self.http = http_client
        self.base_path = "/api/v1/treasury"

    # Positions
    def list_positions(
        self,
        page: int = 1,
        limit: int = 20,
        currency: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List treasury positions.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            currency: Filter by currency

        Returns:
            Paginated list of treasury positions
        """
        params = {
            "page": page,
            "limit": limit,
            "currency": currency,
        }
        return self.http.get(f"{self.base_path}/positions", params=params)

    def get_position(self, position_id: str) -> TreasuryPosition:
        """
        Get treasury position by ID.

        Args:
            position_id: Position ID

        Returns:
            Treasury position details
        """
        return self.http.get(f"{self.base_path}/positions/{position_id}")

    def get_position_by_account(self, account_id: str, currency: str) -> TreasuryPosition:
        """
        Get treasury position for an account and currency.

        Args:
            account_id: Account ID
            currency: Currency code

        Returns:
            Treasury position
        """
        params = {"account_id": account_id, "currency": currency}
        return self.http.get(f"{self.base_path}/positions/by-account", params=params)

    # Liquidity
    def get_liquidity_forecast(
        self,
        account_id: Optional[str] = None,
        days: int = 30,
    ) -> dict:
        """
        Get liquidity forecast.

        Args:
            account_id: Account ID (optional)
            days: Number of days to forecast

        Returns:
            Liquidity forecast
        """
        params = {
            "account_id": account_id,
            "days": days,
        }
        return self.http.get(f"{self.base_path}/liquidity/forecast", params=params)

    def get_cash_flow(
        self,
        account_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get cash flow report.

        Args:
            account_id: Account ID (optional)
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            Cash flow report
        """
        params = {
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(f"{self.base_path}/cash-flow", params=params)

    # Transfers
    def create_transfer(self, data: dict) -> dict:
        """
        Create an internal treasury transfer.

        Args:
            data: Transfer data

        Returns:
            Created transfer
        """
        return self.http.post(f"{self.base_path}/transfers", json=data)

    def list_transfers(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List treasury transfers.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of transfers
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/transfers", params=params)
