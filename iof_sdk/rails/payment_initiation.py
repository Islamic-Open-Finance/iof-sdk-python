"""Payment Initiation Rail API client."""

from typing import Any, Optional


class PaymentInitiationRail:
    """
    Payment Initiation Rail API client.

    Provides payment initiation capabilities:
    - Single payments
    - Payment consents
    - Bulk payments
    - Scheduled payments
    - International payments
    - Payment validation
    - Beneficiary management
    - Payment templates
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Payment Initiation rail client."""
        self.http = http_client
        self.base_path = "/v1/payments"

    # Single Payments

    def create_payment(self, data: dict) -> dict:
        """
        Create a payment.

        Args:
            data: Payment data (accountId, amount, currency, beneficiary, reference)

        Returns:
            Created payment
        """
        return self.http.post(self.base_path, json=data)

    def get_payment(self, payment_id: str) -> dict:
        """
        Get payment by ID.

        Args:
            payment_id: Payment ID

        Returns:
            Payment details
        """
        return self.http.get(f"{self.base_path}/{payment_id}")

    def list_payments(
        self,
        account_id: Optional[str] = None,
        status: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list:
        """
        List payments.

        Args:
            account_id: Filter by account ID
            status: Filter by status
            from_date: Filter from date
            to_date: Filter to date
            limit: Items per page (default: 20)
            offset: Offset (default: 0)

        Returns:
            List of payments
        """
        params = {
            "accountId": account_id,
            "status": status,
            "from": from_date,
            "to": to_date,
            "limit": limit,
            "offset": offset,
        }
        return self.http.get(self.base_path, params=params)

    def cancel_payment(self, payment_id: str) -> dict:
        """
        Cancel a payment.

        Args:
            payment_id: Payment ID

        Returns:
            Cancelled payment
        """
        return self.http.post(f"{self.base_path}/{payment_id}/cancel")

    # Payment Consents

    def create_payment_consent(self, data: dict) -> dict:
        """
        Create a payment consent.

        Args:
            data: Consent data (accountId, amount, currency, beneficiary, reference)

        Returns:
            Created payment consent
        """
        return self.http.post(f"{self.base_path}/consents", json=data)

    def get_payment_consent(self, consent_id: str) -> dict:
        """
        Get payment consent by ID.

        Args:
            consent_id: Consent ID

        Returns:
            Payment consent details
        """
        return self.http.get(f"{self.base_path}/consents/{consent_id}")

    def authorize_payment_consent(
        self, consent_id: str, authorization: dict
    ) -> dict:
        """
        Authorize a payment consent.

        Args:
            consent_id: Consent ID
            authorization: Authorization data (otp, biometric)

        Returns:
            Authorized consent
        """
        return self.http.post(
            f"{self.base_path}/consents/{consent_id}/authorize",
            json=authorization,
        )

    def revoke_payment_consent(self, consent_id: str) -> None:
        """
        Revoke a payment consent.

        Args:
            consent_id: Consent ID
        """
        self.http.delete(f"{self.base_path}/consents/{consent_id}")

    # Bulk Payments

    def create_bulk_payment(self, data: dict) -> dict:
        """
        Create a bulk payment.

        Args:
            data: Bulk payment data (accountId, batchId, payments)

        Returns:
            Created bulk payment
        """
        return self.http.post(f"{self.base_path}/bulk", json=data)

    def get_bulk_payment(self, bulk_payment_id: str) -> dict:
        """
        Get bulk payment by ID.

        Args:
            bulk_payment_id: Bulk payment ID

        Returns:
            Bulk payment details
        """
        return self.http.get(f"{self.base_path}/bulk/{bulk_payment_id}")

    def cancel_bulk_payment(self, bulk_payment_id: str) -> dict:
        """
        Cancel a bulk payment.

        Args:
            bulk_payment_id: Bulk payment ID

        Returns:
            Cancelled bulk payment
        """
        return self.http.post(
            f"{self.base_path}/bulk/{bulk_payment_id}/cancel"
        )

    # Scheduled Payments

    def schedule_payment(self, data: dict) -> dict:
        """
        Schedule a payment.

        Args:
            data: Payment data with scheduledDate and optional recurrence

        Returns:
            Scheduled payment
        """
        return self.http.post(f"{self.base_path}/scheduled", json=data)

    def list_scheduled_payments(self, account_id: str) -> list:
        """
        List scheduled payments for an account.

        Args:
            account_id: Account ID

        Returns:
            List of scheduled payments
        """
        return self.http.get(
            f"/v1/accounts/{account_id}/payments/scheduled"
        )

    def cancel_scheduled_payment(self, payment_id: str) -> None:
        """
        Cancel a scheduled payment.

        Args:
            payment_id: Payment ID
        """
        self.http.delete(f"{self.base_path}/scheduled/{payment_id}")

    # International Payments

    def create_international_payment(self, data: dict) -> dict:
        """
        Create an international payment.

        Args:
            data: Payment data with international beneficiary details

        Returns:
            Created international payment
        """
        return self.http.post(f"{self.base_path}/international", json=data)

    def get_exchange_rate(
        self, from_currency: str, to_currency: str, amount: float
    ) -> dict:
        """
        Get exchange rate.

        Args:
            from_currency: Source currency
            to_currency: Target currency
            amount: Amount

        Returns:
            Exchange rate details
        """
        params = {"from": from_currency, "to": to_currency, "amount": amount}
        return self.http.get(
            f"{self.base_path}/exchange-rates", params=params
        )

    # Payment Validation

    def validate_payment(self, data: dict) -> dict:
        """
        Validate a payment before submission.

        Args:
            data: Payment data to validate

        Returns:
            Validation result (valid, errors, warnings, shariahCompliance, fees)
        """
        return self.http.post(f"{self.base_path}/validate", json=data)

    # Beneficiaries

    def list_beneficiaries(self, account_id: str) -> list:
        """
        List beneficiaries for an account.

        Args:
            account_id: Account ID

        Returns:
            List of beneficiaries
        """
        return self.http.get(f"/v1/accounts/{account_id}/beneficiaries")

    def add_beneficiary(self, account_id: str, beneficiary: dict) -> dict:
        """
        Add a beneficiary.

        Args:
            account_id: Account ID
            beneficiary: Beneficiary data (name, iban, bic, bankName, nickname)

        Returns:
            Created beneficiary
        """
        return self.http.post(
            f"/v1/accounts/{account_id}/beneficiaries", json=beneficiary
        )

    def delete_beneficiary(
        self, account_id: str, beneficiary_id: str
    ) -> None:
        """
        Delete a beneficiary.

        Args:
            account_id: Account ID
            beneficiary_id: Beneficiary ID
        """
        self.http.delete(
            f"/v1/accounts/{account_id}/beneficiaries/{beneficiary_id}"
        )

    # Payment Templates

    def list_payment_templates(self, account_id: str) -> list:
        """
        List payment templates for an account.

        Args:
            account_id: Account ID

        Returns:
            List of payment templates
        """
        return self.http.get(
            f"/v1/accounts/{account_id}/payment-templates"
        )

    def create_payment_template(
        self, account_id: str, template: dict
    ) -> dict:
        """
        Create a payment template.

        Args:
            account_id: Account ID
            template: Template data (name, beneficiaryId, amount, reference)

        Returns:
            Created payment template
        """
        return self.http.post(
            f"/v1/accounts/{account_id}/payment-templates", json=template
        )

    def delete_payment_template(
        self, account_id: str, template_id: str
    ) -> None:
        """
        Delete a payment template.

        Args:
            account_id: Account ID
            template_id: Template ID
        """
        self.http.delete(
            f"/v1/accounts/{account_id}/payment-templates/{template_id}"
        )
