"""Data Quality Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class DataQualityRail:
    """
    Data Quality Rail API client.

    Provides data quality management:
    - Schema validation
    - Referential integrity checks
    - Quality scoring
    - Anomaly detection
    - Quality reports and trends
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Data Quality rail client."""
        self.http = http_client
        self.base_path = "/api/v1/data-quality"

    # Validation

    def validate(self, data: dict) -> dict:
        """
        Validate data against schema.

        Args:
            data: Validation input (entityType, data, schema)

        Returns:
            Validation result with errors and warnings
        """
        return self.http.post(f"{self.base_path}/validate", json=data)

    def validate_referential_integrity(self, data: dict) -> dict:
        """
        Validate referential integrity between entities.

        Args:
            data: Integrity check input (sourceEntity, sourceId, relationships)

        Returns:
            Integrity check result with violations
        """
        return self.http.post(
            f"{self.base_path}/validate/referential-integrity", json=data
        )

    # Quality Scores

    def list_scores(
        self,
        page: int = 1,
        limit: int = 20,
        entity_type: Optional[str] = None,
        min_score: Optional[float] = None,
        max_score: Optional[float] = None,
    ) -> PaginatedResponse:
        """
        List quality scores.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            entity_type: Filter by entity type
            min_score: Filter by minimum score
            max_score: Filter by maximum score

        Returns:
            Paginated list of quality scores
        """
        params = {
            "page": page,
            "limit": limit,
            "entityType": entity_type,
            "minScore": min_score,
            "maxScore": max_score,
        }
        return self.http.get(f"{self.base_path}/scores", params=params)

    def get_scores_by_entity_type(
        self, entity_type: str, page: int = 1, limit: int = 20
    ) -> PaginatedResponse:
        """
        Get quality scores by entity type.

        Args:
            entity_type: Entity type
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of quality scores
        """
        params = {"page": page, "limit": limit}
        return self.http.get(
            f"{self.base_path}/scores/{entity_type}", params=params
        )

    def get_entity_score(self, entity_type: str, entity_id: str) -> dict:
        """
        Get quality score for a specific entity.

        Args:
            entity_type: Entity type
            entity_id: Entity ID

        Returns:
            Quality score details
        """
        return self.http.get(
            f"{self.base_path}/scores/{entity_type}/{entity_id}"
        )

    def calculate_score(self, data: dict) -> dict:
        """
        Calculate quality scores.

        Args:
            data: Score calculation input (entityType, entityIds, dimensions)

        Returns:
            Calculated quality scores
        """
        return self.http.post(f"{self.base_path}/scores/calculate", json=data)

    # Anomalies

    def list_anomalies(
        self,
        page: int = 1,
        limit: int = 20,
        anomaly_type: Optional[str] = None,
        severity: Optional[str] = None,
        status: Optional[str] = None,
        entity_type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List detected anomalies.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            anomaly_type: Filter by anomaly type
            severity: Filter by severity
            status: Filter by status
            entity_type: Filter by entity type

        Returns:
            Paginated list of anomalies
        """
        params = {
            "page": page,
            "limit": limit,
            "type": anomaly_type,
            "severity": severity,
            "status": status,
            "entityType": entity_type,
        }
        return self.http.get(f"{self.base_path}/anomalies", params=params)

    def get_anomaly(self, anomaly_id: str) -> dict:
        """
        Get anomaly by ID.

        Args:
            anomaly_id: Anomaly ID

        Returns:
            Anomaly details
        """
        return self.http.get(f"{self.base_path}/anomalies/{anomaly_id}")

    def acknowledge_anomaly(
        self, anomaly_id: str, notes: Optional[str] = None
    ) -> dict:
        """
        Acknowledge an anomaly.

        Args:
            anomaly_id: Anomaly ID
            notes: Optional notes

        Returns:
            Updated anomaly
        """
        data = {}
        if notes:
            data["notes"] = notes
        return self.http.post(
            f"{self.base_path}/anomalies/{anomaly_id}/acknowledge", json=data
        )

    def resolve_anomaly(
        self,
        anomaly_id: str,
        resolution_notes: str,
        is_false_positive: bool = False,
    ) -> dict:
        """
        Resolve an anomaly.

        Args:
            anomaly_id: Anomaly ID
            resolution_notes: Resolution notes
            is_false_positive: Whether this is a false positive

        Returns:
            Updated anomaly
        """
        data = {
            "resolutionNotes": resolution_notes,
            "isFalsePositive": is_false_positive,
        }
        return self.http.post(
            f"{self.base_path}/anomalies/{anomaly_id}/resolve", json=data
        )

    def detect_anomalies(self, data: dict) -> dict:
        """
        Run anomaly detection.

        Args:
            data: Detection input (entityType, entityIds, types, sensitivity)

        Returns:
            Detected anomalies
        """
        return self.http.post(f"{self.base_path}/detect-anomalies", json=data)

    # Reports

    def list_reports(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List quality reports.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of quality reports
        """
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/reports", params=params)

    def generate_report(self, data: dict) -> dict:
        """
        Generate a quality report.

        Args:
            data: Report generation input (name, entityTypes, startDate, endDate)

        Returns:
            Generated quality report
        """
        return self.http.post(f"{self.base_path}/reports", json=data)

    def get_report(self, report_id: str) -> dict:
        """
        Get quality report by ID.

        Args:
            report_id: Report ID

        Returns:
            Quality report details
        """
        return self.http.get(f"{self.base_path}/reports/{report_id}")

    # Trends

    def get_trends(
        self,
        entity_type: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        granularity: Optional[str] = None,
    ) -> dict:
        """
        Get quality trends.

        Args:
            entity_type: Filter by entity type
            start_date: Start date (ISO format)
            end_date: End date (ISO format)
            granularity: Granularity (day, week, month)

        Returns:
            Quality trend data
        """
        params = {
            "entityType": entity_type,
            "startDate": start_date,
            "endDate": end_date,
            "granularity": granularity,
        }
        return self.http.get(f"{self.base_path}/trends", params=params)
