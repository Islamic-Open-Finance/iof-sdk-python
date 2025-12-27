"""Jurisdictions Rail API client."""

from typing import Any, List

from ..models import Jurisdiction


class JurisdictionsRail:
    """
    Jurisdictions Rail API client.

    Handles multi-jurisdiction regulatory configurations and
    jurisdiction-specific rules.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Jurisdictions rail client."""
        self.http = http_client
        self.base_path = "/api/v1/jurisdictions"

    def list_jurisdictions(self) -> List[Jurisdiction]:
        """
        List all available jurisdictions.

        Returns:
            List of jurisdictions
        """
        return self.http.get(self.base_path)

    def get_jurisdiction(self, jurisdiction_id: str) -> Jurisdiction:
        """
        Get jurisdiction by ID.

        Args:
            jurisdiction_id: Jurisdiction ID

        Returns:
            Jurisdiction details
        """
        return self.http.get(f"{self.base_path}/{jurisdiction_id}")

    def get_jurisdiction_config(self, jurisdiction_id: str) -> dict:
        """
        Get jurisdiction configuration.

        Args:
            jurisdiction_id: Jurisdiction ID

        Returns:
            Jurisdiction configuration
        """
        return self.http.get(f"{self.base_path}/{jurisdiction_id}/config")

    def get_jurisdiction_rules(self, jurisdiction_id: str) -> dict:
        """
        Get jurisdiction-specific rules.

        Args:
            jurisdiction_id: Jurisdiction ID

        Returns:
            Jurisdiction rules
        """
        return self.http.get(f"{self.base_path}/{jurisdiction_id}/rules")
