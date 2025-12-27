"""Search Rail API client."""

from typing import Any, Optional

from ..models import SearchResult


class SearchRail:
    """
    Search Rail API client.

    Provides full-text search across contracts, parties, cases,
    and other entities powered by Meilisearch.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Search rail client."""
        self.http = http_client
        self.base_path = "/api/v1/search"

    def search(
        self,
        query: str,
        index: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
        filters: Optional[dict] = None,
    ) -> SearchResult:
        """
        Perform a search query.

        Args:
            query: Search query string
            index: Search index (contracts, parties, cases, etc.)
            limit: Maximum results to return
            offset: Results offset for pagination
            filters: Additional filters

        Returns:
            Search results
        """
        params = {
            "q": query,
            "index": index,
            "limit": limit,
            "offset": offset,
        }
        if filters:
            params.update(filters)
        return self.http.get(self.base_path, params=params)

    def search_contracts(
        self,
        query: str,
        limit: int = 20,
        filters: Optional[dict] = None,
    ) -> SearchResult:
        """
        Search contracts.

        Args:
            query: Search query string
            limit: Maximum results to return
            filters: Additional filters

        Returns:
            Contract search results
        """
        params = {
            "q": query,
            "limit": limit,
        }
        if filters:
            params.update(filters)
        return self.http.get(f"{self.base_path}/contracts", params=params)

    def search_parties(
        self,
        query: str,
        limit: int = 20,
        filters: Optional[dict] = None,
    ) -> SearchResult:
        """
        Search parties/customers.

        Args:
            query: Search query string
            limit: Maximum results to return
            filters: Additional filters

        Returns:
            Party search results
        """
        params = {
            "q": query,
            "limit": limit,
        }
        if filters:
            params.update(filters)
        return self.http.get(f"{self.base_path}/parties", params=params)

    def search_cases(
        self,
        query: str,
        limit: int = 20,
        filters: Optional[dict] = None,
    ) -> SearchResult:
        """
        Search cases.

        Args:
            query: Search query string
            limit: Maximum results to return
            filters: Additional filters

        Returns:
            Case search results
        """
        params = {
            "q": query,
            "limit": limit,
        }
        if filters:
            params.update(filters)
        return self.http.get(f"{self.base_path}/cases", params=params)

    def suggest(self, query: str, index: Optional[str] = None) -> list:
        """
        Get search suggestions/autocomplete.

        Args:
            query: Partial search query
            index: Search index (optional)

        Returns:
            List of suggestions
        """
        params = {
            "q": query,
            "index": index,
        }
        return self.http.get(f"{self.base_path}/suggest", params=params)

    # Index Management
    def list_indexes(self) -> list:
        """
        List available search indexes.

        Returns:
            List of search indexes
        """
        return self.http.get(f"{self.base_path}/indexes")

    def get_index_stats(self, index: str) -> dict:
        """
        Get search index statistics.

        Args:
            index: Index name

        Returns:
            Index statistics
        """
        return self.http.get(f"{self.base_path}/indexes/{index}/stats")

    def reindex(self, index: str) -> dict:
        """
        Trigger reindexing for an index.

        Args:
            index: Index name

        Returns:
            Reindex job status
        """
        return self.http.post(f"{self.base_path}/indexes/{index}/reindex")
