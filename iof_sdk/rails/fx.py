"""Foreign Exchange (FX) Rail API client."""

from typing import Any, Optional


class FxRail:
    """FX Rail - Shariah-compliant foreign exchange operations."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/fx"

    # Quotes
    def get_quote(self, base_currency: str, quote_currency: str, amount: float) -> dict:
        """Get FX quote."""
        params = {"base": base_currency, "quote": quote_currency, "amount": amount}
        return self.http.get(f"{self.base_path}/quotes", params=params)

    def list_quotes(self, page: int = 1, limit: int = 20) -> dict:
        """List FX quotes."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/quotes", params=params)

    # Trades
    def list_trades(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List FX trades."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/trades", params=params)

    def create_trade(self, data: dict) -> dict:
        """Execute an FX trade."""
        return self.http.post(f"{self.base_path}/trades", json=data)

    def get_trade(self, trade_id: str) -> dict:
        """Get FX trade by ID."""
        return self.http.get(f"{self.base_path}/trades/{trade_id}")

    # Positions
    def list_positions(self) -> dict:
        """List FX positions."""
        return self.http.get(f"{self.base_path}/positions")

    def get_position(self, currency: str) -> dict:
        """Get FX position for a currency."""
        return self.http.get(f"{self.base_path}/positions/{currency}")

    # Exposures
    def list_exposures(self) -> dict:
        """List FX exposures."""
        return self.http.get(f"{self.base_path}/exposures")

    # Limits
    def list_limits(self) -> dict:
        """List FX trading limits."""
        return self.http.get(f"{self.base_path}/limits")

    def update_limits(self, data: dict) -> dict:
        """Update FX trading limits."""
        return self.http.patch(f"{self.base_path}/limits", json=data)
