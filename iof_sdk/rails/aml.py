"""AML/CFT Rail API client."""

from typing import Any, Optional

from ..models import AmlAlert, AmlCase, AmlRule, AmlScreening, PaginatedResponse


class AmlRail:
    """
    AML/CFT Rail API client.

    Handles Anti-Money Laundering and Counter-Terrorist Financing
    compliance including rules, screening, alerts, and cases.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the AML rail client."""
        self.http = http_client
        self.base_path = "/api/v1/aml"

    # Rules
    def list_rules(
        self,
        page: int = 1,
        limit: int = 20,
        enabled: Optional[bool] = None,
    ) -> PaginatedResponse:
        """
        List AML rules.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            enabled: Filter by enabled status

        Returns:
            Paginated list of AML rules
        """
        params = {
            "page": page,
            "limit": limit,
            "enabled": enabled,
        }
        return self.http.get(f"{self.base_path}/rules", params=params)

    def get_rule(self, rule_id: str) -> AmlRule:
        """
        Get AML rule by ID.

        Args:
            rule_id: Rule ID

        Returns:
            AML rule details
        """
        return self.http.get(f"{self.base_path}/rules/{rule_id}")

    def create_rule(self, data: dict) -> AmlRule:
        """
        Create a new AML rule.

        Args:
            data: Rule creation data

        Returns:
            Created AML rule
        """
        return self.http.post(f"{self.base_path}/rules", json=data)

    def update_rule(self, rule_id: str, data: dict) -> AmlRule:
        """
        Update an AML rule.

        Args:
            rule_id: Rule ID
            data: Rule update data

        Returns:
            Updated AML rule
        """
        return self.http.patch(f"{self.base_path}/rules/{rule_id}", json=data)

    def delete_rule(self, rule_id: str) -> None:
        """
        Delete an AML rule.

        Args:
            rule_id: Rule ID
        """
        self.http.delete(f"{self.base_path}/rules/{rule_id}")

    # Screening
    def list_screening(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List AML screening records.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of screening records
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/screening", params=params)

    def get_screening(self, screening_id: str) -> AmlScreening:
        """
        Get screening record by ID.

        Args:
            screening_id: Screening ID

        Returns:
            Screening record details
        """
        return self.http.get(f"{self.base_path}/screening/{screening_id}")

    def create_screening(self, data: dict) -> AmlScreening:
        """
        Create a new screening record.

        Args:
            data: Screening data

        Returns:
            Created screening record
        """
        return self.http.post(f"{self.base_path}/screening", json=data)

    # Alerts
    def list_alerts(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        severity: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List AML alerts.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            severity: Filter by severity

        Returns:
            Paginated list of AML alerts
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "severity": severity,
        }
        return self.http.get(f"{self.base_path}/alerts", params=params)

    def get_alert(self, alert_id: str) -> AmlAlert:
        """
        Get AML alert by ID.

        Args:
            alert_id: Alert ID

        Returns:
            AML alert details
        """
        return self.http.get(f"{self.base_path}/alerts/{alert_id}")

    def create_alert(self, data: dict) -> AmlAlert:
        """
        Create a new AML alert.

        Args:
            data: Alert data

        Returns:
            Created AML alert
        """
        return self.http.post(f"{self.base_path}/alerts", json=data)

    def update_alert(self, alert_id: str, data: dict) -> AmlAlert:
        """
        Update an AML alert.

        Args:
            alert_id: Alert ID
            data: Alert update data

        Returns:
            Updated AML alert
        """
        return self.http.patch(f"{self.base_path}/alerts/{alert_id}", json=data)

    # Cases
    def list_cases(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        priority: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List AML cases.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            priority: Filter by priority

        Returns:
            Paginated list of AML cases
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "priority": priority,
        }
        return self.http.get(f"{self.base_path}/cases", params=params)

    def get_case(self, case_id: str) -> AmlCase:
        """
        Get AML case by ID.

        Args:
            case_id: Case ID

        Returns:
            AML case details
        """
        return self.http.get(f"{self.base_path}/cases/{case_id}")

    def create_case(self, data: dict) -> AmlCase:
        """
        Create a new AML case.

        Args:
            data: Case data

        Returns:
            Created AML case
        """
        return self.http.post(f"{self.base_path}/cases", json=data)

    def update_case(self, case_id: str, data: dict) -> AmlCase:
        """
        Update an AML case.

        Args:
            case_id: Case ID
            data: Case update data

        Returns:
            Updated AML case
        """
        return self.http.patch(f"{self.base_path}/cases/{case_id}", json=data)

    def close_case(self, case_id: str, resolution: str) -> AmlCase:
        """
        Close an AML case.

        Args:
            case_id: Case ID
            resolution: Case resolution

        Returns:
            Closed AML case
        """
        return self.http.post(
            f"{self.base_path}/cases/{case_id}/close", json={"resolution": resolution}
        )
