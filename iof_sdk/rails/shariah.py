"""Shariah Governance & Compliance Rail API client."""

from typing import Any, Optional


class ShariahGovernanceRail:
    """Shariah Governance Rail - board management, rules, and compliance monitoring."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/shariah-governance"

    def list_boards(self, page: int = 1, limit: int = 20) -> dict:
        """List Shariah boards."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/boards", params=params)

    def get_board(self, board_id: str) -> dict:
        """Get Shariah board by ID."""
        return self.http.get(f"{self.base_path}/boards/{board_id}")

    def create_board(self, data: dict) -> dict:
        """Create a Shariah board."""
        return self.http.post(f"{self.base_path}/boards", json=data)

    def list_fatwas(self, page: int = 1, limit: int = 20) -> dict:
        """List fatwas/rulings."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/fatwas", params=params)

    def get_fatwa(self, fatwa_id: str) -> dict:
        """Get fatwa by ID."""
        return self.http.get(f"{self.base_path}/fatwas/{fatwa_id}")


class ShariahRulesRail:
    """Shariah Rules Rail - rule management and evaluation."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/shariah-rules"

    def list_rules(self, page: int = 1, limit: int = 20) -> dict:
        """List Shariah rules."""
        params = {"page": page, "limit": limit}
        return self.http.get(self.base_path, params=params)

    def get_rule(self, rule_id: str) -> dict:
        """Get Shariah rule by ID."""
        return self.http.get(f"{self.base_path}/{rule_id}")

    def create_rule(self, data: dict) -> dict:
        """Create a Shariah rule."""
        return self.http.post(self.base_path, json=data)

    def evaluate(self, data: dict) -> dict:
        """Evaluate data against Shariah rules."""
        return self.http.post(f"{self.base_path}/evaluate", json=data)


class ShariahComplianceRail:
    """Shariah Compliance Rail - compliance checking and monitoring."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/shariah-compliance"

    def check(self, entity_id: str, entity_type: str) -> dict:
        """Check Shariah compliance for an entity."""
        return self.http.post(f"{self.base_path}/check", json={"entity_id": entity_id, "entity_type": entity_type})

    def get_status(self, entity_id: str) -> dict:
        """Get compliance status."""
        return self.http.get(f"{self.base_path}/status/{entity_id}")

    def list_violations(self, page: int = 1, limit: int = 20) -> dict:
        """List compliance violations."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/violations", params=params)
