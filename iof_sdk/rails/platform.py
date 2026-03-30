"""Platform Service Rails API client."""

from typing import Any, Optional


class LiquidityRail:
    """Liquidity management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/liquidity"

    def get_position(self) -> dict:
        """Get liquidity position."""
        return self.http.get(self.base_path)

    def list_pools(self, page: int = 1, limit: int = 20) -> dict:
        """List liquidity pools."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/pools", params=params)

    def forecast(self, data: dict) -> dict:
        """Forecast liquidity needs."""
        return self.http.post(f"{self.base_path}/forecast", json=data)


class ProfitDistributionRail:
    """Profit distribution rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/profit-distribution"

    def list_distributions(self, page: int = 1, limit: int = 20) -> dict:
        """List profit distributions."""
        params = {"page": page, "limit": limit}
        return self.http.get(self.base_path, params=params)

    def calculate(self, data: dict) -> dict:
        """Calculate profit distribution."""
        return self.http.post(f"{self.base_path}/calculate", json=data)

    def distribute(self, distribution_id: str) -> dict:
        """Execute profit distribution."""
        return self.http.post(f"{self.base_path}/{distribution_id}/distribute")


class PaymentsRail:
    """Payment gateway rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/payments"

    def list_payments(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List payments."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_payment(self, payment_id: str) -> dict:
        """Get payment by ID."""
        return self.http.get(f"{self.base_path}/{payment_id}")

    def initiate_payment(self, data: dict) -> dict:
        """Initiate a payment."""
        return self.http.post(self.base_path, json=data)

    def cancel_payment(self, payment_id: str) -> dict:
        """Cancel a payment."""
        return self.http.post(f"{self.base_path}/{payment_id}/cancel")


class DashboardRail:
    """Dashboard analytics rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/dashboard"

    def get_overview(self) -> dict:
        """Get dashboard overview."""
        return self.http.get(self.base_path)

    def get_widgets(self) -> dict:
        """Get dashboard widgets."""
        return self.http.get(f"{self.base_path}/widgets")


class BillingRail:
    """Billing and subscription rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/billing"

    def list_invoices(self, page: int = 1, limit: int = 20) -> dict:
        """List invoices."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/invoices", params=params)

    def get_invoice(self, invoice_id: str) -> dict:
        """Get invoice by ID."""
        return self.http.get(f"{self.base_path}/invoices/{invoice_id}")

    def get_usage(self, period: Optional[str] = None) -> dict:
        """Get usage metrics."""
        params = {"period": period}
        return self.http.get(f"{self.base_path}/usage", params=params)

    def get_subscription(self) -> dict:
        """Get current subscription."""
        return self.http.get(f"{self.base_path}/subscription")


class AuditRail:
    """Audit trail rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/audit"

    def list_logs(self, page: int = 1, limit: int = 20, actor_id: Optional[str] = None, resource_type: Optional[str] = None) -> dict:
        """List audit logs."""
        params = {"page": page, "limit": limit, "actor_id": actor_id, "resource_type": resource_type}
        return self.http.get(self.base_path, params=params)

    def get_log(self, log_id: str) -> dict:
        """Get audit log entry by ID."""
        return self.http.get(f"{self.base_path}/{log_id}")


class WorkspacesRail:
    """Workspaces management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/workspaces"

    def list_workspaces(self, page: int = 1, limit: int = 20) -> dict:
        """List workspaces."""
        params = {"page": page, "limit": limit}
        return self.http.get(self.base_path, params=params)

    def get_workspace(self, workspace_id: str) -> dict:
        """Get workspace by ID."""
        return self.http.get(f"{self.base_path}/{workspace_id}")

    def create_workspace(self, data: dict) -> dict:
        """Create a workspace."""
        return self.http.post(self.base_path, json=data)

    def update_workspace(self, workspace_id: str, data: dict) -> dict:
        """Update a workspace."""
        return self.http.patch(f"{self.base_path}/{workspace_id}", json=data)

    def list_members(self, workspace_id: str) -> dict:
        """List workspace members."""
        return self.http.get(f"{self.base_path}/{workspace_id}/members")

    def add_member(self, workspace_id: str, data: dict) -> dict:
        """Add a workspace member."""
        return self.http.post(f"{self.base_path}/{workspace_id}/members", json=data)


class MetadataRail:
    """Metadata and taxonomy rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/metadata"

    def list_schemas(self) -> dict:
        """List metadata schemas."""
        return self.http.get(f"{self.base_path}/schemas")

    def get_schema(self, schema_id: str) -> dict:
        """Get metadata schema by ID."""
        return self.http.get(f"{self.base_path}/schemas/{schema_id}")


class ReferenceDataRail:
    """Reference data rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/reference-data"

    def list_currencies(self) -> dict:
        """List supported currencies."""
        return self.http.get(f"{self.base_path}/currencies")

    def list_countries(self) -> dict:
        """List supported countries."""
        return self.http.get(f"{self.base_path}/countries")

    def list_contract_types(self) -> dict:
        """List Islamic contract types."""
        return self.http.get(f"{self.base_path}/contract-types")
