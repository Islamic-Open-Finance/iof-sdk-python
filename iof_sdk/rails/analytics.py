"""Analytics Rail API client."""

from typing import Any, Optional


class AnalyticsRail:
    """
    Analytics Rail API client.

    Provides advanced analytics and business intelligence capabilities.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Analytics rail client."""
        self.http = http_client
        self.base_path = "/api/v1/analytics"

    # Contracts Analytics
    def get_contracts_overview(
        self,
        from_date: str,
        to_date: str,
        bank_id: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
        contract_type: Optional[str] = None,
    ) -> dict:
        """
        Get contracts analytics overview.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            bank_id: Filter by bank ID
            jurisdiction_id: Filter by jurisdiction
            contract_type: Filter by contract type

        Returns:
            Contracts overview analytics
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "bank_id": bank_id,
            "jurisdiction_id": jurisdiction_id,
            "contract_type": contract_type,
        }
        return self.http.get(f"{self.base_path}/contracts/overview", params=params)

    def get_contracts_exposure(
        self,
        bank_id: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
        contract_type: Optional[str] = None,
    ) -> dict:
        """
        Get contracts exposure analytics.

        Args:
            bank_id: Filter by bank ID
            jurisdiction_id: Filter by jurisdiction
            contract_type: Filter by contract type

        Returns:
            Contracts exposure analytics
        """
        params = {
            "bank_id": bank_id,
            "jurisdiction_id": jurisdiction_id,
            "contract_type": contract_type,
        }
        return self.http.get(f"{self.base_path}/contracts/exposure", params=params)

    # Shariah Analytics
    def get_shariah_flags(
        self,
        from_date: str,
        to_date: str,
        flag_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> dict:
        """
        Get Shariah flags analytics.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            flag_type: Filter by flag type
            status: Filter by status

        Returns:
            Shariah flags analytics
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "flag_type": flag_type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/shariah/flags", params=params)

    def get_shariah_heatmap(
        self,
        from_date: str,
        to_date: str,
        bank_id: Optional[str] = None,
    ) -> dict:
        """
        Get Shariah compliance heatmap.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            bank_id: Filter by bank ID

        Returns:
            Shariah compliance heatmap
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "bank_id": bank_id,
        }
        return self.http.get(f"{self.base_path}/shariah/heatmap", params=params)

    # Reconciliation Analytics
    def get_reconciliation_exceptions(
        self,
        from_date: str,
        to_date: str,
        exception_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> dict:
        """
        Get reconciliation exceptions analytics.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            exception_type: Filter by exception type
            status: Filter by status

        Returns:
            Reconciliation exceptions analytics
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "exception_type": exception_type,
            "status": status,
        }
        return self.http.get(
            f"{self.base_path}/reconciliation/exceptions", params=params
        )

    # Usage Analytics
    def get_usage_metrics(
        self,
        from_date: str,
        to_date: str,
        rail_name: Optional[str] = None,
        group_by: Optional[str] = None,
    ) -> dict:
        """
        Get API usage metrics.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            rail_name: Filter by rail name
            group_by: Group by dimension (day, hour, rail, endpoint)

        Returns:
            Usage metrics
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "rail_name": rail_name,
            "group_by": group_by,
        }
        return self.http.get(f"{self.base_path}/usage/metrics", params=params)

    def get_usage_by_rail(
        self,
        from_date: str,
        to_date: str,
        bank_id: Optional[str] = None,
    ) -> dict:
        """
        Get usage broken down by rail.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            bank_id: Filter by bank ID

        Returns:
            Usage by rail
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "bank_id": bank_id,
        }
        return self.http.get(f"{self.base_path}/usage/by-rail", params=params)

    # Billing Analytics
    def get_billing_aggregates(
        self,
        from_date: str,
        to_date: str,
        bank_id: Optional[str] = None,
        sku_id: Optional[str] = None,
    ) -> dict:
        """
        Get billing aggregates.

        Args:
            from_date: Start date (ISO format)
            to_date: End date (ISO format)
            bank_id: Filter by bank ID
            sku_id: Filter by SKU ID

        Returns:
            Billing aggregates
        """
        params = {
            "from_date": from_date,
            "to_date": to_date,
            "bank_id": bank_id,
            "sku_id": sku_id,
        }
        return self.http.get(f"{self.base_path}/billing/aggregates", params=params)

    # Custom Analytics
    def execute_custom_query(self, view_name: str, filters: Optional[dict] = None) -> dict:
        """
        Execute a custom analytics query.

        Args:
            view_name: Name of the analytics view
            filters: Optional filters

        Returns:
            Query results
        """
        data = {
            "view_name": view_name,
            "filters": filters or {},
        }
        return self.http.post(f"{self.base_path}/custom", json=data)
