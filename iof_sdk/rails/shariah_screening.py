"""Shariah Screening Rail API client."""

from typing import Any, Optional


class ShariahScreeningRail:
    """Shariah compliance screening for securities and financial products rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/shariah-screening"

    def screen_security(self, data: dict) -> dict:
        """Screen a security or instrument for Shariah compliance."""
        return self.http.post(f"{self.base_path}/screen", json=data)

    def screen_batch(self, data: dict) -> dict:
        """Screen a batch of securities for Shariah compliance."""
        return self.http.post(f"{self.base_path}/screen/batch", json=data)

    def get_screening_result(self, result_id: str) -> dict:
        """Get a Shariah screening result by ID."""
        return self.http.get(f"{self.base_path}/results/{result_id}")

    def list_screening_results(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        standard: Optional[str] = None,
    ) -> dict:
        """List Shariah screening results."""
        params = {"page": page, "limit": limit, "status": status, "standard": standard}
        return self.http.get(f"{self.base_path}/results", params=params)

    def list_criteria(self, standard: Optional[str] = None) -> dict:
        """List Shariah screening criteria by standard (AAOIFI, DJIM, etc.)."""
        params = {"standard": standard}
        return self.http.get(f"{self.base_path}/criteria", params=params)

    def get_criterion(self, criterion_id: str) -> dict:
        """Get a specific Shariah screening criterion."""
        return self.http.get(f"{self.base_path}/criteria/{criterion_id}")

    def get_watchlist(self, page: int = 1, limit: int = 20) -> dict:
        """Get the list of Shariah non-compliant securities on watch."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/watchlist", params=params)

    def add_to_watchlist(self, data: dict) -> dict:
        """Add a security to the Shariah non-compliant watchlist."""
        return self.http.post(f"{self.base_path}/watchlist", json=data)

    def remove_from_watchlist(self, security_id: str) -> dict:
        """Remove a security from the watchlist."""
        return self.http.delete(f"{self.base_path}/watchlist/{security_id}")

    def get_purification_rate(self, security_id: str) -> dict:
        """Get the income purification rate for a security."""
        return self.http.get(f"{self.base_path}/purification/{security_id}")
