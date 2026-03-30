"""Agent Rail — Deterministic agent execution client."""

from typing import Any, Dict, List, Literal, Optional

from ..base_client import BaseClient


AgentType = Literal[
    "kyc_router",
    "compliance_triage",
    "recon_break",
    "evidence_pack",
]


class AgentRailClient:
    """Client for executing deterministic agents via the Agent Rail API."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def execute(
        self,
        tenant_id: str,
        workspace_id: str,
        agent_type: AgentType,
        input_data: Dict[str, Any],
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Execute an agent by type."""
        return self._client.post(
            "/agents/execute",
            json={
                "tenant_id": tenant_id,
                "workspace_id": workspace_id,
                "agent_type": agent_type,
                "input": input_data,
                "correlation_id": correlation_id,
            },
        )

    def route_kyc(
        self,
        tenant_id: str,
        workspace_id: str,
        input_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Route a KYC case to the correct queue."""
        return self._client.post(
            "/agents/kyc-router",
            json={
                "tenant_id": tenant_id,
                "workspace_id": workspace_id,
                "input": input_data,
            },
        )

    def triage_compliance_alert(
        self,
        tenant_id: str,
        workspace_id: str,
        input_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Triage a compliance alert."""
        return self._client.post(
            "/agents/compliance-triage",
            json={
                "tenant_id": tenant_id,
                "workspace_id": workspace_id,
                "input": input_data,
            },
        )

    def handle_recon_break(
        self,
        tenant_id: str,
        workspace_id: str,
        input_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Handle a reconciliation break."""
        return self._client.post(
            "/agents/recon-break",
            json={
                "tenant_id": tenant_id,
                "workspace_id": workspace_id,
                "input": input_data,
            },
        )

    def build_evidence_pack(
        self,
        tenant_id: str,
        workspace_id: str,
        input_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Build a compliance evidence pack."""
        return self._client.post(
            "/agents/evidence-pack",
            json={
                "tenant_id": tenant_id,
                "workspace_id": workspace_id,
                "input": input_data,
            },
        )

    def validate_transition(
        self,
        from_state: str,
        to_state: str,
        entity_type: str = "case",
    ) -> Dict[str, Any]:
        """Validate a state machine transition."""
        return self._client.post(
            "/agents/validate-transition",
            json={
                "from_state": from_state,
                "to_state": to_state,
                "entity_type": entity_type,
            },
        )

    def evaluate_policy(
        self,
        subject: Dict[str, Any],
        resource: Dict[str, Any],
        action: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Evaluate a policy decision."""
        return self._client.post(
            "/agents/evaluate-policy",
            json={
                "subject": subject,
                "resource": resource,
                "action": action,
                "context": context or {},
            },
        )
