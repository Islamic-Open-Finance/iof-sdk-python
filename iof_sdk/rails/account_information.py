"""Account Information Rail - AIS (Account Information Services)."""

from typing import Any, Dict, List, Optional


class Account:
    """Bank account representation."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self.id = data.get("id")
        self.account_number = data.get("accountNumber")
        self.account_type = data.get("accountType")
        self.currency = data.get("currency")
        self.balance = data.get("balance", {})
        self.status = data.get("status")
        self.ownership = data.get("ownership", {})
        self.islamic_compliance = data.get("islamicCompliance", {})
        self.created = data.get("created")
        self.updated = data.get("updated")


class Transaction:
    """Transaction representation."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self.id = data.get("id")
        self.account_id = data.get("accountId")
        self.type = data.get("type")
        self.amount = data.get("amount")
        self.currency = data.get("currency")
        self.description = data.get("description")
        self.category = data.get("category")
        self.merchant = data.get("merchant")
        self.balance = data.get("balance", {})
        self.shariah_compliance = data.get("shariahCompliance", {})
        self.timestamp = data.get("timestamp")


class Statement:
    """Account statement."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self.account_id = data.get("accountId")
        self.period = data.get("period", {})
        self.summary = data.get("summary", {})
        self.transactions = [Transaction(t) for t in data.get("transactions", [])]
        self.zakat_calculation = data.get("zakatCalculation")


class AccountInformationRail:
    """Account Information Services rail client.

    Handles account listing, transactions, statements, zakat calculations,
    standing orders, and direct debits.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Account Information rail client."""
        self.http = http_client
        self.base_path = "/api/v1/accounts"

    def list_accounts(
        self,
        user_id: Optional[str] = None,
        account_type: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> List[Account]:
        """List all accounts."""
        params = {
            "userId": user_id,
            "type": account_type,
            "status": status,
            "limit": limit,
            "offset": offset,
        }
        response = self.http.get(self.base_path, params=params)
        return [Account(a) for a in response]

    def get_account(self, account_id: str) -> Account:
        """Get account details."""
        response = self.http.get(f"{self.base_path}/{account_id}")
        return Account(response)

    def get_account_balance(self, account_id: str) -> Dict[str, Any]:
        """Get account balance."""
        return self.http.get(f"{self.base_path}/{account_id}/balance")

    def list_transactions(
        self,
        account_id: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        transaction_type: Optional[str] = None,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        category: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> List[Transaction]:
        """List account transactions."""
        params = {
            "from": from_date,
            "to": to_date,
            "type": transaction_type,
            "minAmount": min_amount,
            "maxAmount": max_amount,
            "category": category,
            "limit": limit,
            "offset": offset,
        }
        response = self.http.get(f"{self.base_path}/{account_id}/transactions", params=params)
        return [Transaction(t) for t in response]

    def get_transaction(self, account_id: str, transaction_id: str) -> Transaction:
        """Get transaction details."""
        response = self.http.get(f"{self.base_path}/{account_id}/transactions/{transaction_id}")
        return Transaction(response)

    def search_transactions(
        self,
        account_id: str,
        text: Optional[str] = None,
        merchant: Optional[str] = None,
        category: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> List[Transaction]:
        """Search transactions."""
        query = {
            "text": text,
            "merchant": merchant,
            "category": category,
            "from": from_date,
            "to": to_date,
        }
        response = self.http.post(f"{self.base_path}/{account_id}/transactions/search", json=query)
        return [Transaction(t) for t in response]

    def get_statement(
        self,
        account_id: str,
        from_date: str,
        to_date: str,
        format: str = "json",
    ) -> Statement:
        """Get account statement."""
        params = {"from": from_date, "to": to_date, "format": format}
        response = self.http.get(f"{self.base_path}/{account_id}/statements", params=params)
        return Statement(response)

    def download_statement(
        self,
        account_id: str,
        from_date: str,
        to_date: str,
        format: str = "pdf",
    ) -> bytes:
        """Download account statement as bytes."""
        params = {"from": from_date, "to": to_date, "format": format}
        return self.http.get(f"{self.base_path}/{account_id}/statements/download", params=params, stream=True)

    def calculate_zakat(
        self,
        account_id: str,
        as_of: Optional[str] = None,
        nisab: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Calculate zakat for account."""
        body = {"asOf": as_of, "nisab": nisab}
        return self.http.post(f"{self.base_path}/{account_id}/zakat/calculate", json=body)

    def get_zakat_history(
        self,
        account_id: str,
        year: Optional[int] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Get zakat calculation history."""
        params = {"year": year, "limit": limit}
        return self.http.get(f"{self.base_path}/{account_id}/zakat/history", params=params)

    def verify_account(
        self,
        account_id: str,
        verification_type: str,
        value: str,
    ) -> Dict[str, Any]:
        """Verify account details."""
        body = {"type": verification_type, "value": value}
        return self.http.post(f"{self.base_path}/{account_id}/verify", json=body)

    def list_standing_orders(self, account_id: str) -> List[Dict[str, Any]]:
        """List standing orders."""
        return self.http.get(f"{self.base_path}/{account_id}/standing-orders")

    def create_standing_order(
        self,
        account_id: str,
        beneficiary_id: str,
        amount: float,
        frequency: str,
        start_date: str,
        end_date: Optional[str] = None,
        reference: str = "",
    ) -> Dict[str, Any]:
        """Create standing order."""
        body = {
            "beneficiaryId": beneficiary_id,
            "amount": amount,
            "frequency": frequency,
            "startDate": start_date,
            "endDate": end_date,
            "reference": reference,
        }
        return self.http.post(f"{self.base_path}/{account_id}/standing-orders", json=body)

    def cancel_standing_order(self, account_id: str, order_id: str) -> None:
        """Cancel standing order."""
        self.http.delete(f"{self.base_path}/{account_id}/standing-orders/{order_id}")

    def list_direct_debits(self, account_id: str) -> List[Dict[str, Any]]:
        """List direct debits."""
        return self.http.get(f"{self.base_path}/{account_id}/direct-debits")

    def cancel_direct_debit(self, account_id: str, debit_id: str) -> None:
        """Cancel direct debit."""
        self.http.delete(f"{self.base_path}/{account_id}/direct-debits/{debit_id}")

    def get_account_limits(self, account_id: str) -> Dict[str, Any]:
        """Get account limits."""
        return self.http.get(f"{self.base_path}/{account_id}/limits")

    def update_account_limits(
        self,
        account_id: str,
        daily_transfer_limit: Optional[float] = None,
        monthly_transfer_limit: Optional[float] = None,
        single_transaction_limit: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Update account limits."""
        body = {
            "dailyTransferLimit": daily_transfer_limit,
            "monthlyTransferLimit": monthly_transfer_limit,
            "singleTransactionLimit": single_transaction_limit,
        }
        return self.http.patch(f"{self.base_path}/{account_id}/limits", json=body)


# Backward compatibility alias
AccountInformationClient = AccountInformationRail
