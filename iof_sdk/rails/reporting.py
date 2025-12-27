"""Reporting Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, Report


class ReportingRail:
    """
    Reporting Rail API client.

    Handles report generation, dashboards, and analytics.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Reporting rail client."""
        self.http = http_client
        self.base_path = "/api/v1/reporting"

    # Reports
    def list_reports(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List generated reports.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by report type
            status: Filter by status

        Returns:
            Paginated list of reports
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/reports", params=params)

    def get_report(self, report_id: str) -> Report:
        """
        Get report by ID.

        Args:
            report_id: Report ID

        Returns:
            Report details
        """
        return self.http.get(f"{self.base_path}/reports/{report_id}")

    def generate_report(self, data: dict) -> Report:
        """
        Generate a new report.

        Args:
            data: Report generation parameters

        Returns:
            Generated report
        """
        return self.http.post(f"{self.base_path}/reports", json=data)

    def download_report(self, report_id: str) -> dict:
        """
        Get report download URL.

        Args:
            report_id: Report ID

        Returns:
            Download URL and metadata
        """
        return self.http.get(f"{self.base_path}/reports/{report_id}/download")

    # Templates
    def list_templates(self) -> list:
        """
        List available report templates.

        Returns:
            List of report templates
        """
        return self.http.get(f"{self.base_path}/templates")

    def get_template(self, template_id: str) -> dict:
        """
        Get report template by ID.

        Args:
            template_id: Template ID

        Returns:
            Template details
        """
        return self.http.get(f"{self.base_path}/templates/{template_id}")

    # Dashboards
    def list_dashboards(self) -> list:
        """
        List available dashboards.

        Returns:
            List of dashboards
        """
        return self.http.get(f"{self.base_path}/dashboards")

    def get_dashboard(self, dashboard_id: str) -> dict:
        """
        Get dashboard by ID.

        Args:
            dashboard_id: Dashboard ID

        Returns:
            Dashboard configuration and data
        """
        return self.http.get(f"{self.base_path}/dashboards/{dashboard_id}")

    def get_dashboard_data(
        self,
        dashboard_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get dashboard data.

        Args:
            dashboard_id: Dashboard ID
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            Dashboard data
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(
            f"{self.base_path}/dashboards/{dashboard_id}/data", params=params
        )

    # Scheduled Reports
    def list_scheduled_reports(self) -> list:
        """
        List scheduled reports.

        Returns:
            List of scheduled reports
        """
        return self.http.get(f"{self.base_path}/scheduled")

    def create_scheduled_report(self, data: dict) -> dict:
        """
        Create a scheduled report.

        Args:
            data: Schedule configuration

        Returns:
            Created schedule
        """
        return self.http.post(f"{self.base_path}/scheduled", json=data)

    def delete_scheduled_report(self, schedule_id: str) -> None:
        """
        Delete a scheduled report.

        Args:
            schedule_id: Schedule ID
        """
        self.http.delete(f"{self.base_path}/scheduled/{schedule_id}")
