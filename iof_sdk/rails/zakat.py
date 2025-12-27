"""Zakat & Purification Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse, ZakatCalculation, ZakatPayment


class ZakatRail:
    """
    Zakat & Purification Rail API client.

    Handles zakat calculation, payment tracking, and purification
    of prohibited income.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Zakat rail client."""
        self.http = http_client
        self.base_path = "/api/v1/zakat"

    # Calculations
    def list_calculations(
        self,
        page: int = 1,
        limit: int = 20,
        year: Optional[int] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List zakat calculations.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            year: Filter by year
            status: Filter by status

        Returns:
            Paginated list of zakat calculations
        """
        params = {
            "page": page,
            "limit": limit,
            "year": year,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/calculations", params=params)

    def get_calculation(self, calculation_id: str) -> ZakatCalculation:
        """
        Get zakat calculation by ID.

        Args:
            calculation_id: Calculation ID

        Returns:
            Zakat calculation details
        """
        return self.http.get(f"{self.base_path}/calculations/{calculation_id}")

    def create_calculation(self, data: dict) -> ZakatCalculation:
        """
        Create a new zakat calculation.

        Args:
            data: Calculation data

        Returns:
            Created zakat calculation
        """
        return self.http.post(f"{self.base_path}/calculations", json=data)

    def calculate_zakat(self, account_id: str, year: int) -> ZakatCalculation:
        """
        Calculate zakat for an account.

        Args:
            account_id: Account ID
            year: Year for calculation

        Returns:
            Zakat calculation
        """
        return self.http.post(
            f"{self.base_path}/calculate",
            json={"account_id": account_id, "year": year},
        )

    # Payments
    def list_payments(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List zakat payments.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of zakat payments
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/payments", params=params)

    def get_payment(self, payment_id: str) -> ZakatPayment:
        """
        Get zakat payment by ID.

        Args:
            payment_id: Payment ID

        Returns:
            Zakat payment details
        """
        return self.http.get(f"{self.base_path}/payments/{payment_id}")

    def create_payment(self, data: dict) -> ZakatPayment:
        """
        Record a zakat payment.

        Args:
            data: Payment data

        Returns:
            Created zakat payment
        """
        return self.http.post(f"{self.base_path}/payments", json=data)

    # Purification
    def calculate_purification(self, account_id: str, year: int) -> dict:
        """
        Calculate purification amount for prohibited income.

        Args:
            account_id: Account ID
            year: Year for calculation

        Returns:
            Purification calculation
        """
        return self.http.post(
            f"{self.base_path}/purification/calculate",
            json={"account_id": account_id, "year": year},
        )

    def get_nisab_rates(self, currency: str = "USD") -> dict:
        """
        Get current nisab rates.

        Args:
            currency: Currency code (default: USD)

        Returns:
            Nisab rates
        """
        params = {"currency": currency}
        return self.http.get(f"{self.base_path}/nisab", params=params)
