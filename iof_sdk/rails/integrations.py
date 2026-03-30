"""Integrations Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class IntegrationsRail:
    """
    Integrations Rail API client.

    Provides integration management:
    - Connector registration and lifecycle
    - Sync job orchestration
    - Data mapping configuration
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Integrations rail client."""
        self.http = http_client
        self.base_path = "/api/v1/integrations"

    # Connectors

    def list_connectors(
        self,
        page: int = 1,
        limit: int = 20,
        connector_type: Optional[str] = None,
        status: Optional[str] = None,
        search: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List connectors.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            connector_type: Filter by connector type
            status: Filter by status
            search: Search query

        Returns:
            Paginated list of connectors
        """
        params = {
            "page": page,
            "limit": limit,
            "type": connector_type,
            "status": status,
            "search": search,
        }
        return self.http.get(f"{self.base_path}/connectors", params=params)

    def create_connector(self, data: dict) -> dict:
        """
        Create a new connector.

        Args:
            data: Connector creation data (name, type, config)

        Returns:
            Created connector
        """
        return self.http.post(f"{self.base_path}/connectors", json=data)

    def get_connector(self, connector_id: str) -> dict:
        """
        Get connector by ID.

        Args:
            connector_id: Connector ID

        Returns:
            Connector details
        """
        return self.http.get(f"{self.base_path}/connectors/{connector_id}")

    def update_connector(self, connector_id: str, data: dict) -> dict:
        """
        Update a connector.

        Args:
            connector_id: Connector ID
            data: Update data

        Returns:
            Updated connector
        """
        return self.http.patch(
            f"{self.base_path}/connectors/{connector_id}", json=data
        )

    def delete_connector(self, connector_id: str) -> None:
        """
        Delete a connector.

        Args:
            connector_id: Connector ID
        """
        self.http.delete(f"{self.base_path}/connectors/{connector_id}")

    def test_connection(self, connector_id: str) -> dict:
        """
        Test a connector connection.

        Args:
            connector_id: Connector ID

        Returns:
            Connection test result
        """
        return self.http.post(
            f"{self.base_path}/connectors/{connector_id}/test"
        )

    def enable_connector(self, connector_id: str) -> dict:
        """
        Enable a connector.

        Args:
            connector_id: Connector ID

        Returns:
            Updated connector
        """
        return self.http.post(
            f"{self.base_path}/connectors/{connector_id}/enable"
        )

    def disable_connector(self, connector_id: str) -> dict:
        """
        Disable a connector.

        Args:
            connector_id: Connector ID

        Returns:
            Updated connector
        """
        return self.http.post(
            f"{self.base_path}/connectors/{connector_id}/disable"
        )

    # Sync Jobs

    def list_sync_jobs(
        self,
        page: int = 1,
        limit: int = 20,
        connector_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List sync jobs.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            connector_id: Filter by connector ID
            status: Filter by status

        Returns:
            Paginated list of sync jobs
        """
        params = {
            "page": page,
            "limit": limit,
            "connectorId": connector_id,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/sync-jobs", params=params)

    def start_sync(self, data: dict) -> dict:
        """
        Start a sync job.

        Args:
            data: Sync job data (connectorId, mappingId, mode, options)

        Returns:
            Created sync job
        """
        return self.http.post(f"{self.base_path}/sync-jobs", json=data)

    def get_job_status(self, job_id: str) -> dict:
        """
        Get sync job status.

        Args:
            job_id: Job ID

        Returns:
            Sync job details
        """
        return self.http.get(f"{self.base_path}/sync-jobs/{job_id}")

    def pause_sync(self, job_id: str) -> dict:
        """
        Pause a sync job.

        Args:
            job_id: Job ID

        Returns:
            Updated sync job
        """
        return self.http.post(f"{self.base_path}/sync-jobs/{job_id}/pause")

    def resume_sync(self, job_id: str) -> dict:
        """
        Resume a paused sync job.

        Args:
            job_id: Job ID

        Returns:
            Updated sync job
        """
        return self.http.post(f"{self.base_path}/sync-jobs/{job_id}/resume")

    def cancel_sync(self, job_id: str) -> dict:
        """
        Cancel a sync job.

        Args:
            job_id: Job ID

        Returns:
            Cancelled sync job
        """
        return self.http.post(f"{self.base_path}/sync-jobs/{job_id}/cancel")

    def get_sync_history(
        self, job_id: str, page: int = 1, limit: int = 20
    ) -> PaginatedResponse:
        """
        Get sync job history.

        Args:
            job_id: Job ID
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            Paginated list of sync history entries
        """
        params = {"page": page, "limit": limit}
        return self.http.get(
            f"{self.base_path}/sync-jobs/{job_id}/history", params=params
        )

    # Mappings

    def list_mappings(
        self,
        page: int = 1,
        limit: int = 20,
        connector_id: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> PaginatedResponse:
        """
        List data mappings.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            connector_id: Filter by connector ID
            is_active: Filter by active status

        Returns:
            Paginated list of data mappings
        """
        params = {
            "page": page,
            "limit": limit,
            "connectorId": connector_id,
            "isActive": is_active,
        }
        return self.http.get(f"{self.base_path}/mappings", params=params)

    def create_mapping(self, data: dict) -> dict:
        """
        Create a data mapping.

        Args:
            data: Mapping data

        Returns:
            Created mapping
        """
        return self.http.post(f"{self.base_path}/mappings", json=data)

    def get_mapping(self, mapping_id: str) -> dict:
        """
        Get data mapping by ID.

        Args:
            mapping_id: Mapping ID

        Returns:
            Mapping details
        """
        return self.http.get(f"{self.base_path}/mappings/{mapping_id}")

    def update_mapping(self, mapping_id: str, data: dict) -> dict:
        """
        Update a data mapping.

        Args:
            mapping_id: Mapping ID
            data: Update data

        Returns:
            Updated mapping
        """
        return self.http.patch(
            f"{self.base_path}/mappings/{mapping_id}", json=data
        )

    def delete_mapping(self, mapping_id: str) -> None:
        """
        Delete a data mapping.

        Args:
            mapping_id: Mapping ID
        """
        self.http.delete(f"{self.base_path}/mappings/{mapping_id}")

    def validate_mapping(
        self, mapping_id: str, sample_data: Optional[list] = None
    ) -> dict:
        """
        Validate a data mapping.

        Args:
            mapping_id: Mapping ID
            sample_data: Optional sample data for validation

        Returns:
            Validation result
        """
        data = {}
        if sample_data:
            data["sampleData"] = sample_data
        return self.http.post(
            f"{self.base_path}/mappings/{mapping_id}/validate", json=data
        )
