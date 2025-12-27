"""Underwriting Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, UnderwritingDecision


class UnderwritingRail:
    """
    Underwriting Rail API client.

    Handles credit and risk assessment for financing applications.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Underwriting rail client."""
        self.http = http_client
        self.base_path = "/api/v1/underwriting"

    # Applications
    def list_applications(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List underwriting applications.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of applications
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/applications", params=params)

    def get_application(self, application_id: str) -> dict:
        """
        Get underwriting application by ID.

        Args:
            application_id: Application ID

        Returns:
            Application details
        """
        return self.http.get(f"{self.base_path}/applications/{application_id}")

    def create_application(self, data: dict) -> dict:
        """
        Create a new underwriting application.

        Args:
            data: Application data

        Returns:
            Created application
        """
        return self.http.post(f"{self.base_path}/applications", json=data)

    def submit_application(self, application_id: str) -> dict:
        """
        Submit an application for underwriting.

        Args:
            application_id: Application ID

        Returns:
            Submitted application
        """
        return self.http.post(f"{self.base_path}/applications/{application_id}/submit")

    # Decisions
    def list_decisions(
        self,
        page: int = 1,
        limit: int = 20,
        decision: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List underwriting decisions.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            decision: Filter by decision (approved/declined)

        Returns:
            Paginated list of decisions
        """
        params = {
            "page": page,
            "limit": limit,
            "decision": decision,
        }
        return self.http.get(f"{self.base_path}/decisions", params=params)

    def get_decision(self, decision_id: str) -> UnderwritingDecision:
        """
        Get underwriting decision by ID.

        Args:
            decision_id: Decision ID

        Returns:
            Decision details
        """
        return self.http.get(f"{self.base_path}/decisions/{decision_id}")

    def make_decision(self, application_id: str, data: dict) -> UnderwritingDecision:
        """
        Make an underwriting decision.

        Args:
            application_id: Application ID
            data: Decision data

        Returns:
            Created decision
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/decide", json=data
        )

    # Risk Scoring
    def calculate_risk_score(self, application_id: str) -> dict:
        """
        Calculate risk score for an application.

        Args:
            application_id: Application ID

        Returns:
            Risk score calculation
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/risk-score"
        )

    def get_credit_report(self, customer_id: str) -> dict:
        """
        Get credit report for a customer.

        Args:
            customer_id: Customer ID

        Returns:
            Credit report
        """
        params = {"customer_id": customer_id}
        return self.http.get(f"{self.base_path}/credit-report", params=params)
