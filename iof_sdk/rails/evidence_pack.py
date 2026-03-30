"""Evidence Pack Rail API client."""

from typing import Any, Optional


class EvidencePackRail:
    """Regulatory evidence pack generation and management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/evidence-pack"

    def list_packs(self, page: int = 1, limit: int = 20, standard: Optional[str] = None) -> dict:
        """List evidence packs."""
        params = {"page": page, "limit": limit, "standard": standard}
        return self.http.get(self.base_path, params=params)

    def get_pack(self, pack_id: str) -> dict:
        """Get evidence pack by ID."""
        return self.http.get(f"{self.base_path}/{pack_id}")

    def generate_pack(self, data: dict) -> dict:
        """Generate a new evidence pack for a compliance standard."""
        return self.http.post(self.base_path, json=data)

    def download_pack(self, pack_id: str) -> dict:
        """Download evidence pack as archive."""
        return self.http.get(f"{self.base_path}/{pack_id}/download")

    def list_artifacts(self, pack_id: str) -> dict:
        """List artifacts included in an evidence pack."""
        return self.http.get(f"{self.base_path}/{pack_id}/artifacts")

    def add_artifact(self, pack_id: str, data: dict) -> dict:
        """Add an artifact to an evidence pack."""
        return self.http.post(f"{self.base_path}/{pack_id}/artifacts", json=data)

    def get_attestation(self, pack_id: str) -> dict:
        """Get compliance attestation for an evidence pack."""
        return self.http.get(f"{self.base_path}/{pack_id}/attestation")

    def sign_attestation(self, pack_id: str, data: dict) -> dict:
        """Sign compliance attestation for an evidence pack."""
        return self.http.post(f"{self.base_path}/{pack_id}/attestation/sign", json=data)
