"""Taxonomy Rail API client."""

from typing import Any, Optional


class TaxonomyRail:
    """Islamic finance taxonomy, classifications, and ontology rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/taxonomy"

    def list_categories(self, page: int = 1, limit: int = 20, parent_id: Optional[str] = None) -> dict:
        """List taxonomy categories."""
        params = {"page": page, "limit": limit, "parent_id": parent_id}
        return self.http.get(f"{self.base_path}/categories", params=params)

    def get_category(self, category_id: str) -> dict:
        """Get taxonomy category by ID."""
        return self.http.get(f"{self.base_path}/categories/{category_id}")

    def create_category(self, data: dict) -> dict:
        """Create a taxonomy category."""
        return self.http.post(f"{self.base_path}/categories", json=data)

    def update_category(self, category_id: str, data: dict) -> dict:
        """Update a taxonomy category."""
        return self.http.patch(f"{self.base_path}/categories/{category_id}", json=data)

    def list_tags(self, page: int = 1, limit: int = 20) -> dict:
        """List taxonomy tags."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/tags", params=params)

    def get_tag(self, tag_id: str) -> dict:
        """Get taxonomy tag by ID."""
        return self.http.get(f"{self.base_path}/tags/{tag_id}")

    def create_tag(self, data: dict) -> dict:
        """Create a taxonomy tag."""
        return self.http.post(f"{self.base_path}/tags", json=data)

    def search_taxonomy(self, query: str, limit: int = 20) -> dict:
        """Search across taxonomy categories and tags."""
        params = {"q": query, "limit": limit}
        return self.http.get(f"{self.base_path}/search", params=params)

    def get_contract_taxonomy(self, contract_type: str) -> dict:
        """Get taxonomy classification for an Islamic contract type."""
        return self.http.get(f"{self.base_path}/contracts/{contract_type}")
