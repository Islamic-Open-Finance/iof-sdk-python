"""Prudential & Basel III Compliance Rail API client."""

from typing import Any, Optional


class PrudentialRail:
    """Prudential Rail - Basel III capital adequacy, liquidity, leverage, and regulatory reporting."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1"

    # Prudential Governance
    def get_governance_metrics(self) -> dict:
        """Get prudential governance metrics."""
        return self.http.get(f"{self.base_path}/prudential/governance/metrics")

    def get_data_lineage(self, entity_id: str) -> dict:
        """Get data lineage for an entity."""
        return self.http.get(f"{self.base_path}/prudential/governance/lineage/{entity_id}")

    def get_data_quality(self) -> dict:
        """Get data quality metrics."""
        return self.http.get(f"{self.base_path}/prudential/governance/dq")

    def list_attestations(self, page: int = 1, limit: int = 20) -> dict:
        """List attestations."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/prudential/governance/attestations", params=params)

    def create_attestation(self, data: dict) -> dict:
        """Create an attestation."""
        return self.http.post(f"{self.base_path}/prudential/governance/attestations", json=data)

    def generate_evidence_pack(self, data: dict) -> dict:
        """Generate evidence pack for auditors."""
        return self.http.post(f"{self.base_path}/prudential/governance/evidence-packs", json=data)

    # Basel Liquidity
    def list_liquidity_runs(self, page: int = 1, limit: int = 20) -> dict:
        """List Basel liquidity runs (LCR/NSFR)."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/basel/liquidity/runs", params=params)

    def create_liquidity_run(self, data: dict) -> dict:
        """Create a liquidity calculation run."""
        return self.http.post(f"{self.base_path}/basel/liquidity/runs", json=data)

    def list_assumption_sets(self) -> dict:
        """List liquidity assumption sets."""
        return self.http.get(f"{self.base_path}/basel/liquidity/assumption-sets")

    # Basel Exposures
    def list_exposure_snapshots(self, page: int = 1, limit: int = 20) -> dict:
        """List exposure snapshots."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/basel/exposures/snapshots", params=params)

    def list_exposure_limits(self) -> dict:
        """List exposure limits."""
        return self.http.get(f"{self.base_path}/basel/exposures/limits")

    def list_exposure_breaches(self, page: int = 1, limit: int = 20) -> dict:
        """List exposure breaches."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/basel/exposures/breaches", params=params)

    # Basel Capital
    def list_capital_components(self) -> dict:
        """List capital components (CET1, AT1, T2)."""
        return self.http.get(f"{self.base_path}/basel/capital/components")

    def get_rwa(self) -> dict:
        """Get Risk-Weighted Assets (RWA)."""
        return self.http.get(f"{self.base_path}/basel/capital/rwa")

    def create_capital_run(self, data: dict) -> dict:
        """Create a capital adequacy calculation run."""
        return self.http.post(f"{self.base_path}/basel/capital/runs", json=data)

    # Basel Leverage
    def create_leverage_run(self, data: dict) -> dict:
        """Create a leverage ratio calculation run."""
        return self.http.post(f"{self.base_path}/basel/leverage/runs", json=data)

    # Pillar 2 - ICAAP
    def list_icaap_plans(self, page: int = 1, limit: int = 20) -> dict:
        """List ICAAP plans."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/pillar2/icaap/plans", params=params)

    def list_stress_scenarios(self) -> dict:
        """List stress scenarios."""
        return self.http.get(f"{self.base_path}/pillar2/icaap/stress-scenarios")

    def create_icaap_run(self, data: dict) -> dict:
        """Create an ICAAP run."""
        return self.http.post(f"{self.base_path}/pillar2/icaap/runs", json=data)

    # Pillar 3 - Disclosures
    def list_disclosure_templates(self) -> dict:
        """List Pillar 3 disclosure templates."""
        return self.http.get(f"{self.base_path}/pillar3/templates")

    def create_disclosure_run(self, data: dict) -> dict:
        """Create a Pillar 3 disclosure run."""
        return self.http.post(f"{self.base_path}/pillar3/disclosures/runs", json=data)

    def export_disclosure(self, run_id: str, format: str = "xlsx") -> bytes:
        """Export a disclosure report."""
        params = {"format": format}
        return self.http.get(f"{self.base_path}/pillar3/disclosures/exports/{run_id}", params=params, stream=True)
