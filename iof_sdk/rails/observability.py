"""Observability Rail API client."""

from typing import Any, Optional

from ..models import (
    AuditLog,
    DataExport,
    PaginatedResponse,
    ShariahMonitoringRecord,
    SloMetric,
)


class ObservabilityRail:
    """
    Observability Rail API client.

    Handles SLOs, audit logs, Shariah monitoring, and data export.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Observability rail client."""
        self.http = http_client
        self.base_path = "/api/v1/observability"

    # SLOs (Service Level Objectives)
    def list_slos(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List SLO metrics.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of SLO metrics
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/slos", params=params)

    def get_slo(self, slo_id: str) -> SloMetric:
        """
        Get SLO metric by ID.

        Args:
            slo_id: SLO ID

        Returns:
            SLO metric details
        """
        return self.http.get(f"{self.base_path}/slos/{slo_id}")

    def get_slo_summary(self) -> dict:
        """
        Get SLO summary across all metrics.

        Returns:
            SLO summary
        """
        return self.http.get(f"{self.base_path}/slos/summary")

    # Audit Logs
    def list_audit_logs(
        self,
        page: int = 1,
        limit: int = 20,
        event_type: Optional[str] = None,
        resource_type: Optional[str] = None,
        actor_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List audit logs with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            event_type: Filter by event type
            resource_type: Filter by resource type
            actor_id: Filter by actor ID
            start_date: Filter by start date (ISO format)
            end_date: Filter by end date (ISO format)

        Returns:
            Paginated list of audit logs
        """
        params = {
            "page": page,
            "limit": limit,
            "event_type": event_type,
            "resource_type": resource_type,
            "actor_id": actor_id,
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(f"{self.base_path}/audit-logs", params=params)

    def get_audit_log(self, log_id: str) -> AuditLog:
        """
        Get audit log by ID.

        Args:
            log_id: Audit log ID

        Returns:
            Audit log details
        """
        return self.http.get(f"{self.base_path}/audit-logs/{log_id}")

    def export_audit_logs(
        self,
        start_date: str,
        end_date: str,
        format: str = "json",
    ) -> DataExport:
        """
        Export audit logs.

        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)
            format: Export format (json, csv)

        Returns:
            Data export job
        """
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "format": format,
        }
        return self.http.post(f"{self.base_path}/audit-logs/export", json=data)

    # Shariah Monitoring
    def list_shariah_monitoring(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        check_type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List Shariah monitoring records.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            check_type: Filter by check type

        Returns:
            Paginated list of monitoring records
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "check_type": check_type,
        }
        return self.http.get(f"{self.base_path}/shariah-monitoring", params=params)

    def get_shariah_monitoring(self, record_id: str) -> ShariahMonitoringRecord:
        """
        Get Shariah monitoring record by ID.

        Args:
            record_id: Record ID

        Returns:
            Monitoring record details
        """
        return self.http.get(f"{self.base_path}/shariah-monitoring/{record_id}")

    def run_shariah_check(self, contract_id: str, check_type: str) -> ShariahMonitoringRecord:
        """
        Run a Shariah compliance check on a contract.

        Args:
            contract_id: Contract ID
            check_type: Type of check to run

        Returns:
            Monitoring record
        """
        data = {
            "contract_id": contract_id,
            "check_type": check_type,
        }
        return self.http.post(f"{self.base_path}/shariah-monitoring/check", json=data)

    # Data Export
    def list_exports(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List data export jobs.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of export jobs
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/exports", params=params)

    def get_export(self, export_id: str) -> DataExport:
        """
        Get data export job by ID.

        Args:
            export_id: Export ID

        Returns:
            Export job details
        """
        return self.http.get(f"{self.base_path}/exports/{export_id}")

    def create_export(self, data: dict) -> DataExport:
        """
        Create a new data export job.

        Args:
            data: Export configuration

        Returns:
            Created export job
        """
        return self.http.post(f"{self.base_path}/exports", json=data)

    def download_export(self, export_id: str) -> dict:
        """
        Get download URL for an export.

        Args:
            export_id: Export ID

        Returns:
            Download URL and metadata
        """
        return self.http.get(f"{self.base_path}/exports/{export_id}/download")

    # Health & Metrics
    def get_health(self) -> dict:
        """
        Get system health status.

        Returns:
            Health status
        """
        return self.http.get(f"{self.base_path}/health")

    def get_metrics(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get system metrics.

        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            System metrics
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(f"{self.base_path}/metrics", params=params)
