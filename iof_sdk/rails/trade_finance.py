"""Trade Finance Rail API client."""

from typing import Any, Optional


class TradeFinanceRail:
    """Trade Finance Rail - letters of credit, guarantees, documentary collections, supply chain."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/trade"

    # Letters of Credit
    def list_lcs(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List letters of credit."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/lc", params=params)

    def get_lc(self, lc_id: str) -> dict:
        """Get letter of credit by ID."""
        return self.http.get(f"{self.base_path}/lc/{lc_id}")

    def create_lc(self, data: dict) -> dict:
        """Create a letter of credit."""
        return self.http.post(f"{self.base_path}/lc", json=data)

    # Guarantees
    def list_guarantees(self, page: int = 1, limit: int = 20) -> dict:
        """List trade guarantees."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/guarantees", params=params)

    def create_guarantee(self, data: dict) -> dict:
        """Create a trade guarantee."""
        return self.http.post(f"{self.base_path}/guarantees", json=data)

    # Documentary Collections
    def list_documentary(self, page: int = 1, limit: int = 20) -> dict:
        """List documentary collections."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/documentary", params=params)

    def create_documentary(self, data: dict) -> dict:
        """Create a documentary collection."""
        return self.http.post(f"{self.base_path}/documentary", json=data)

    # Supply Chain Finance
    def list_supply_chain(self, page: int = 1, limit: int = 20) -> dict:
        """List supply chain finance programs."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/supply-chain", params=params)

    def create_supply_chain(self, data: dict) -> dict:
        """Create a supply chain finance program."""
        return self.http.post(f"{self.base_path}/supply-chain", json=data)

    # Presentations
    def list_presentations(self, page: int = 1, limit: int = 20) -> dict:
        """List trade document presentations."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/presentations", params=params)

    def create_presentation(self, data: dict) -> dict:
        """Create a trade document presentation."""
        return self.http.post(f"{self.base_path}/presentations", json=data)
