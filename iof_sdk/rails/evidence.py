"""Evidence Engine Rail API client.

Moat namespace covering signed compliance pack export + one-call verification.
Covers 47/54 controls across SOC 2, ISO 27001, AAOIFI, GDPR, PSD2, IFSB,
ISO 20022. Every pack is a SHA-256 Merkle tree with HMAC signature; auditors
verify with a single API call (no portal). Reclaims 30-55 bps on audit and
re-papering cycles.
"""

from typing import Any, Optional


class EvidenceRail:
    """Evidence Engine — signed compliance pack export + verification.

    Methods are thin HTTP wrappers around the /api/v1/evidence endpoints.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Evidence rail client."""
        self.http = http_client
        self.base_path = "/api/v1/evidence"

    # ------------------------------------------------------------------
    # Export (signed pack)
    # ------------------------------------------------------------------
    def export(
        self,
        format: str,
        trade_id: Optional[str] = None,
        contract_id: Optional[str] = None,
        **kwargs: Any,
    ) -> dict:
        """Export a signed evidence pack for a trade or contract.

        Args:
            format: Output format — one of ``json``, ``csv``, ``pdf``, ``zip``.
            trade_id: Trade identifier (mutually exclusive with contract_id).
            contract_id: Contract identifier (mutually exclusive with trade_id).
            **kwargs: Additional fields forwarded to the API.

        Returns:
            EvidencePack — signed pack metadata including Merkle root and HMAC.
        """
        if not trade_id and not contract_id:
            raise ValueError("export requires either trade_id or contract_id")
        body: dict = {"format": format}
        if trade_id is not None:
            body["tradeId"] = trade_id
        if contract_id is not None:
            body["contractId"] = contract_id
        body.update(kwargs)
        return self.http.post(f"{self.base_path}/export", json=body)

    # ------------------------------------------------------------------
    # One-call verification
    # ------------------------------------------------------------------
    def verify(
        self,
        pack_id: str,
        merkle_root: str,
        signature: str,
    ) -> dict:
        """Verify an evidence pack against its Merkle root + HMAC signature.

        Args:
            pack_id: Pack identifier returned by ``export``.
            merkle_root: Hex-encoded SHA-256 Merkle root.
            signature: HMAC signature (base64 or hex).

        Returns:
            EvidenceVerifyResult — verification status, mismatched leaves (if any).
        """
        return self.http.post(
            f"{self.base_path}/verify",
            json={
                "packId": pack_id,
                "merkleRoot": merkle_root,
                "signature": signature,
            },
        )

    # ------------------------------------------------------------------
    # Control catalogue
    # ------------------------------------------------------------------
    def get_controls(self, framework: Optional[str] = None) -> dict:
        """List compliance frameworks and the control IDs each covers.

        Args:
            framework: Optional filter — e.g. ``SOC2``, ``ISO27001``,
                ``AAOIFI``, ``GDPR``, ``PSD2``, ``IFSB``, ``ISO20022``.

        Returns:
            EvidenceControlCatalogue — frameworks → controls mapping.
        """
        params: dict = {}
        if framework is not None:
            params["framework"] = framework
        return self.http.get(f"{self.base_path}/controls", params=params)

    # ------------------------------------------------------------------
    # Listing / retrieval
    # ------------------------------------------------------------------
    def list(
        self,
        trade_id: Optional[str] = None,
        contract_id: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """List evidence packs with optional filters (trade, contract, window)."""
        params: dict = {}
        if trade_id is not None:
            params["tradeId"] = trade_id
        if contract_id is not None:
            params["contractId"] = contract_id
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to
        if limit is not None:
            params["limit"] = limit
        return self.http.get(self.base_path, params=params)

    def get(self, pack_id: str) -> dict:
        """Get a single evidence pack by ID."""
        return self.http.get(f"{self.base_path}/{pack_id}")

    def download(self, pack_id: str) -> dict:
        """Download the raw artifact for an evidence pack (signed bundle)."""
        return self.http.get(f"{self.base_path}/{pack_id}/download")
