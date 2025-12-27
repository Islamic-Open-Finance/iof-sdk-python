"""Compliance Rail API client."""

from typing import Any, Optional

from ..models import ComplianceCheck, PaginatedResponse


class ComplianceRail:
    """
    Compliance Rail API client.

    Handles regulatory and Shariah compliance monitoring and reporting.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Compliance rail client."""
        self.http = http_client
        self.base_path = "/api/v1/compliance"

    # Checks
    def list_checks(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List compliance checks.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by check type
            status: Filter by status

        Returns:
            Paginated list of compliance checks
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/checks", params=params)

    def get_check(self, check_id: str) -> ComplianceCheck:
        """
        Get compliance check by ID.

        Args:
            check_id: Check ID

        Returns:
            Compliance check details
        """
        return self.http.get(f"{self.base_path}/checks/{check_id}")

    def create_check(self, data: dict) -> ComplianceCheck:
        """
        Create a new compliance check.

        Args:
            data: Check data

        Returns:
            Created compliance check
        """
        return self.http.post(f"{self.base_path}/checks", json=data)

    def run_check(self, check_id: str) -> ComplianceCheck:
        """
        Run a compliance check.

        Args:
            check_id: Check ID

        Returns:
            Check result
        """
        return self.http.post(f"{self.base_path}/checks/{check_id}/run")

    # Rules
    def list_rules(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> PaginatedResponse:
        """
        List compliance rules.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by rule type
            enabled: Filter by enabled status

        Returns:
            Paginated list of compliance rules
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "enabled": enabled,
        }
        return self.http.get(f"{self.base_path}/rules", params=params)

    def get_rule(self, rule_id: str) -> dict:
        """
        Get compliance rule by ID.

        Args:
            rule_id: Rule ID

        Returns:
            Rule details
        """
        return self.http.get(f"{self.base_path}/rules/{rule_id}")

    def create_rule(self, data: dict) -> dict:
        """
        Create a new compliance rule.

        Args:
            data: Rule creation data

        Returns:
            Created rule
        """
        return self.http.post(f"{self.base_path}/rules", json=data)

    def update_rule(self, rule_id: str, data: dict) -> dict:
        """
        Update a compliance rule.

        Args:
            rule_id: Rule ID
            data: Rule update data

        Returns:
            Updated rule
        """
        return self.http.patch(f"{self.base_path}/rules/{rule_id}", json=data)

    # Reports
    def generate_compliance_report(self, data: dict) -> dict:
        """
        Generate a compliance report.

        Args:
            data: Report parameters

        Returns:
            Generated report
        """
        return self.http.post(f"{self.base_path}/reports", json=data)

    def get_compliance_status(
        self,
        entity_id: Optional[str] = None,
        entity_type: Optional[str] = None,
    ) -> dict:
        """
        Get compliance status summary.

        Args:
            entity_id: Entity ID (optional)
            entity_type: Entity type (optional)

        Returns:
            Compliance status
        """
        params = {
            "entity_id": entity_id,
            "entity_type": entity_type,
        }
        return self.http.get(f"{self.base_path}/status", params=params)
