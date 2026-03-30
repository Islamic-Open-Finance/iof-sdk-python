"""Audit Analytics Rail API client."""

from typing import Any, Optional


class AuditAnalyticsRail:
    """Audit trail analytics, querying, and reporting rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/audit-analytics"

    def query_events(self, data: dict) -> dict:
        """Query audit events with filters and aggregations."""
        return self.http.post(f"{self.base_path}/query", json=data)

    def get_event(self, event_id: str) -> dict:
        """Get a specific audit event by ID."""
        return self.http.get(f"{self.base_path}/events/{event_id}")

    def list_events(
        self,
        page: int = 1,
        limit: int = 20,
        actor_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        action: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> dict:
        """List audit events with optional filtering."""
        params = {
            "page": page,
            "limit": limit,
            "actor_id": actor_id,
            "resource_type": resource_type,
            "action": action,
            "from": from_date,
            "to": to_date,
        }
        return self.http.get(f"{self.base_path}/events", params=params)

    def get_summary(self, period: Optional[str] = None) -> dict:
        """Get audit event summary statistics for a period."""
        params = {"period": period}
        return self.http.get(f"{self.base_path}/summary", params=params)

    def get_actor_activity(self, actor_id: str, page: int = 1, limit: int = 20) -> dict:
        """Get activity timeline for a specific actor."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/actors/{actor_id}/activity", params=params)

    def get_resource_history(self, resource_type: str, resource_id: str) -> dict:
        """Get complete change history for a specific resource."""
        return self.http.get(f"{self.base_path}/resources/{resource_type}/{resource_id}")

    def export_report(self, data: dict) -> dict:
        """Export an audit report in a specified format (CSV, PDF, JSON)."""
        return self.http.post(f"{self.base_path}/export", json=data)

    def get_anomalies(self, page: int = 1, limit: int = 20) -> dict:
        """Get detected anomalous audit events."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/anomalies", params=params)
