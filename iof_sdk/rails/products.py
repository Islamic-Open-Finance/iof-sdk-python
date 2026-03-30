"""Products Rail API client."""

from typing import Any, Optional


class ProductsRail:
    """Islamic financial product catalogue and configuration rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/products"

    def list_products(self, page: int = 1, limit: int = 20, category: Optional[str] = None) -> dict:
        """List financial products."""
        params = {"page": page, "limit": limit, "category": category}
        return self.http.get(self.base_path, params=params)

    def get_product(self, product_id: str) -> dict:
        """Get product by ID."""
        return self.http.get(f"{self.base_path}/{product_id}")

    def create_product(self, data: dict) -> dict:
        """Create a new financial product."""
        return self.http.post(self.base_path, json=data)

    def update_product(self, product_id: str, data: dict) -> dict:
        """Update a financial product."""
        return self.http.patch(f"{self.base_path}/{product_id}", json=data)

    def delete_product(self, product_id: str) -> dict:
        """Delete a financial product."""
        return self.http.delete(f"{self.base_path}/{product_id}")

    def publish_product(self, product_id: str) -> dict:
        """Publish a product to make it available."""
        return self.http.post(f"{self.base_path}/{product_id}/publish")

    def archive_product(self, product_id: str) -> dict:
        """Archive a product."""
        return self.http.post(f"{self.base_path}/{product_id}/archive")

    def list_variants(self, product_id: str) -> dict:
        """List product variants."""
        return self.http.get(f"{self.base_path}/{product_id}/variants")

    def get_shariah_disclosure(self, product_id: str) -> dict:
        """Get Shariah disclosure for a product."""
        return self.http.get(f"{self.base_path}/{product_id}/shariah-disclosure")
