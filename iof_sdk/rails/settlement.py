"""Settlement Engine Rail API client.

Moat namespace covering 24x7x365 DvP / FOP / RVP / DFP atomic settlement.
Aligns with AAOIFI SS-1 (Trading in Currencies), SS-8 (Murabaha), SS-10 (Salam),
SS-17 (Investment Sukuk), SS-21 (Financial Papers), SS-30 (Monetisation),
plus CSDR Article 7 settlement discipline. Ribawi-aware netting reclaims
60-140 bps per corridor versus conventional rails.
"""

from typing import Any, Optional


class SettlementRail:
    """Settlement Engine — atomic settlement, finality, and netting.

    Methods are thin HTTP wrappers around the /api/v1/settlement endpoints.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Settlement rail client."""
        self.http = http_client
        self.base_path = "/api/v1/settlement"

    # ------------------------------------------------------------------
    # Atomic confirmation (DvP / FOP / RVP / DFP)
    # ------------------------------------------------------------------
    def confirm(
        self,
        contract_id: str,
        mode: str,
        parties: list,
        amount: Optional[float] = None,
        currency: Optional[str] = None,
        **kwargs: Any,
    ) -> dict:
        """Atomically confirm a settlement across DvP / FOP / RVP / DFP.

        Args:
            contract_id: Underlying contract or trade identifier.
            mode: Settlement mode — one of ``DvP``, ``FOP``, ``RVP``, ``DFP``.
            parties: List of settlement parties (deliverer / receiver).
            amount: Settlement amount (optional for FOP).
            currency: ISO 4217 currency code.
            **kwargs: Additional fields forwarded to the API.

        Returns:
            SettlementResult — settlement record with state machine state and
            AAOIFI standard references.
        """
        body: dict = {
            "contractId": contract_id,
            "mode": mode,
            "parties": parties,
        }
        if amount is not None:
            body["amount"] = amount
        if currency is not None:
            body["currency"] = currency
        body.update(kwargs)
        return self.http.post(f"{self.base_path}/confirm", json=body)

    # ------------------------------------------------------------------
    # Status / lifecycle
    # ------------------------------------------------------------------
    def get_status(self, settlement_id: str) -> dict:
        """Return settlement status with state machine state + AAOIFI references."""
        return self.http.get(f"{self.base_path}/{settlement_id}/status")

    def get(self, settlement_id: str) -> dict:
        """Get a single settlement record by ID."""
        return self.http.get(f"{self.base_path}/{settlement_id}")

    def cancel(self, settlement_id: str, reason: str) -> dict:
        """Cancel a settlement before finality.

        Post-finality cancellations require an unwind workflow.
        """
        return self.http.post(
            f"{self.base_path}/{settlement_id}/cancel",
            json={"reason": reason},
        )

    def finalize(self, settlement_id: str) -> dict:
        """Mark a settlement as final (CSDR Art. 7 finality timestamp)."""
        return self.http.post(f"{self.base_path}/{settlement_id}/finalize")

    # ------------------------------------------------------------------
    # Listing
    # ------------------------------------------------------------------
    def list(
        self,
        status: Optional[str] = None,
        contract_id: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> dict:
        """List settlements with optional filters (status, contract, window)."""
        params: dict = {}
        if status is not None:
            params["status"] = status
        if contract_id is not None:
            params["contractId"] = contract_id
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to
        if limit is not None:
            params["limit"] = limit
        return self.http.get(self.base_path, params=params)

    # ------------------------------------------------------------------
    # Ribawi-aware netting (AAOIFI SS-1 + SS-30)
    # ------------------------------------------------------------------
    def netting(
        self,
        corridor: str,
        pair: str,
        window: str,
        **kwargs: Any,
    ) -> dict:
        """Compute ribawi-aware netting for a corridor / pair / window.

        Honours AAOIFI SS-1 (Trading in Currencies) and SS-30 (Monetisation)
        constraints — sarf legs are excluded from net-set eligibility.

        Args:
            corridor: Settlement corridor identifier (e.g. ``GCC-EU``).
            pair: Currency / asset pair (e.g. ``USD/AED``).
            window: Netting window (ISO 8601 duration or named cycle).

        Returns:
            SettlementNettingResult — gross vs net obligations, savings bps.
        """
        body: dict = {"corridor": corridor, "pair": pair, "window": window}
        body.update(kwargs)
        return self.http.post(f"{self.base_path}/netting", json=body)
