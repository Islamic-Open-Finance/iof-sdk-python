"""Routing Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, RoutingRule


class RoutingRail:
    """
    Routing Rail API client.

    Handles payment and message routing rules and routing decisions.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Routing rail client."""
        self.http = http_client
        self.base_path = "/api/v1/routing"

    def list_rules(
        self,
        page: int = 1,
        limit: int = 20,
        enabled: Optional[bool] = None,
    ) -> PaginatedResponse:
        """
        List routing rules.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            enabled: Filter by enabled status

        Returns:
            Paginated list of routing rules
        """
        params = {
            "page": page,
            "limit": limit,
            "enabled": enabled,
        }
        return self.http.get(f"{self.base_path}/rules", params=params)

    def get_rule(self, rule_id: str) -> RoutingRule:
        """
        Get routing rule by ID.

        Args:
            rule_id: Rule ID

        Returns:
            Routing rule details
        """
        return self.http.get(f"{self.base_path}/rules/{rule_id}")

    def create_rule(self, data: dict) -> RoutingRule:
        """
        Create a new routing rule.

        Args:
            data: Rule creation data

        Returns:
            Created routing rule
        """
        return self.http.post(f"{self.base_path}/rules", json=data)

    def update_rule(self, rule_id: str, data: dict) -> RoutingRule:
        """
        Update a routing rule.

        Args:
            rule_id: Rule ID
            data: Rule update data

        Returns:
            Updated routing rule
        """
        return self.http.patch(f"{self.base_path}/rules/{rule_id}", json=data)

    def delete_rule(self, rule_id: str) -> None:
        """
        Delete a routing rule.

        Args:
            rule_id: Rule ID
        """
        self.http.delete(f"{self.base_path}/rules/{rule_id}")

    def enable_rule(self, rule_id: str) -> RoutingRule:
        """
        Enable a routing rule.

        Args:
            rule_id: Rule ID

        Returns:
            Enabled rule
        """
        return self.http.post(f"{self.base_path}/rules/{rule_id}/enable")

    def disable_rule(self, rule_id: str) -> RoutingRule:
        """
        Disable a routing rule.

        Args:
            rule_id: Rule ID

        Returns:
            Disabled rule
        """
        return self.http.post(f"{self.base_path}/rules/{rule_id}/disable")

    def evaluate_routing(self, transaction_data: dict) -> dict:
        """
        Evaluate routing for a transaction.

        Args:
            transaction_data: Transaction data to route

        Returns:
            Routing decision
        """
        return self.http.post(f"{self.base_path}/evaluate", json=transaction_data)

    def test_rule(self, rule_id: str, test_data: dict) -> dict:
        """
        Test a routing rule with sample data.

        Args:
            rule_id: Rule ID
            test_data: Test transaction data

        Returns:
            Test result
        """
        return self.http.post(
            f"{self.base_path}/rules/{rule_id}/test", json=test_data
        )
