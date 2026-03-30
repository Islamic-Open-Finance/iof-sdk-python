"""Sukuk (Islamic Capital Markets) Rail API client."""

from typing import Any, Optional


class SukukRail:
    """Sukuk Rail - Islamic bond issuance, trading, settlement, and compliance."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/sukuk"

    # Issuance
    def list_issuances(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Sukuk issuances."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/issuance", params=params)

    def get_issuance(self, issuance_id: str) -> dict:
        """Get Sukuk issuance by ID."""
        return self.http.get(f"{self.base_path}/issuance/{issuance_id}")

    def create_issuance(self, data: dict) -> dict:
        """Create a new Sukuk issuance."""
        return self.http.post(f"{self.base_path}/issuance", json=data)

    # Trading
    def list_trades(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List Sukuk trades."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/trading", params=params)

    def create_trade(self, data: dict) -> dict:
        """Create a Sukuk trade."""
        return self.http.post(f"{self.base_path}/trading", json=data)

    # Settlement
    def list_settlements(self, page: int = 1, limit: int = 20) -> dict:
        """List Sukuk settlements."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/settlement", params=params)

    def settle(self, trade_id: str) -> dict:
        """Settle a Sukuk trade."""
        return self.http.post(f"{self.base_path}/settlement", json={"trade_id": trade_id})

    # Corporate Actions
    def list_corporate_actions(self, page: int = 1, limit: int = 20) -> dict:
        """List corporate actions."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/corporate-actions", params=params)

    # Valuation
    def get_valuation(self, sukuk_id: str) -> dict:
        """Get Sukuk valuation."""
        return self.http.get(f"{self.base_path}/valuation/{sukuk_id}")

    # Compliance
    def check_compliance(self, sukuk_id: str) -> dict:
        """Check Sukuk Shariah compliance."""
        return self.http.get(f"{self.base_path}/compliance/{sukuk_id}")
