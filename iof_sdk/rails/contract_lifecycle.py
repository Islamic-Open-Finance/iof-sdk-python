"""Contract Lifecycle Rail API client."""

from typing import Any, Optional


class ContractLifecycleRail:
    """Contract Lifecycle Rail - lifecycle management, amendments, and renewals."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/contract-lifecycle"

    def get_lifecycle(self, contract_id: str) -> dict:
        """Get contract lifecycle state."""
        return self.http.get(f"{self.base_path}/{contract_id}")

    def transition(self, contract_id: str, action: str, data: Optional[dict] = None) -> dict:
        """Transition contract to next lifecycle stage."""
        body = {"action": action}
        if data:
            body.update(data)
        return self.http.post(f"{self.base_path}/{contract_id}/transition", json=body)

    def list_amendments(self, contract_id: str) -> dict:
        """List contract amendments."""
        return self.http.get(f"{self.base_path}/{contract_id}/amendments")

    def create_amendment(self, contract_id: str, data: dict) -> dict:
        """Create a contract amendment."""
        return self.http.post(f"{self.base_path}/{contract_id}/amendments", json=data)

    def renew(self, contract_id: str, data: dict) -> dict:
        """Renew a contract."""
        return self.http.post(f"{self.base_path}/{contract_id}/renew", json=data)

    def terminate(self, contract_id: str, reason: str) -> dict:
        """Terminate a contract."""
        return self.http.post(f"{self.base_path}/{contract_id}/terminate", json={"reason": reason})
