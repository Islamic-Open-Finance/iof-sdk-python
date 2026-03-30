"""ISO 20022 Rail API client."""

from typing import Any, Optional


class ISO20022Rail:
    """
    ISO 20022 Rail API client.

    Provides ISO 20022 financial messaging capabilities:
    - Credit transfer initiation (pain.001)
    - Payment status reports (pacs.002)
    - Account statements (camt.053)
    - Message validation
    - Market practice configurations
    - Islamic finance extensions
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the ISO 20022 rail client."""
        self.http = http_client
        self.base_path = "/api/v1/rails/iso20022"

    # Credit Transfer Operations

    def create_credit_transfer(self, data: dict) -> dict:
        """
        Create a customer credit transfer initiation (pain.001).

        Args:
            data: Credit transfer data (marketPractice, creditTransfer, validateOnly)

        Returns:
            Created message with validation result
        """
        return self.http.post(f"{self.base_path}/credit-transfers", json=data)

    def get_credit_transfer(self, message_id: str) -> dict:
        """
        Get credit transfer by message ID.

        Args:
            message_id: Message ID

        Returns:
            ISO 20022 message details
        """
        return self.http.get(f"{self.base_path}/credit-transfers/{message_id}")

    def cancel_credit_transfer(
        self, message_id: str, code: str, description: Optional[str] = None
    ) -> dict:
        """
        Cancel a credit transfer (camt.056).

        Args:
            message_id: Message ID
            code: Cancellation reason code
            description: Optional description

        Returns:
            Cancellation message
        """
        data = {"code": code, "description": description}
        return self.http.post(
            f"{self.base_path}/credit-transfers/{message_id}/cancel", json=data
        )

    # Status Operations

    def get_message_status(self, message_id: str) -> dict:
        """
        Get message status.

        Args:
            message_id: Message ID

        Returns:
            Message status with status report
        """
        return self.http.get(
            f"{self.base_path}/messages/{message_id}/status"
        )

    def get_transaction_status_by_uetr(self, uetr: str) -> dict:
        """
        Get transaction status by UETR.

        Args:
            uetr: Universal End-to-End Transaction Reference

        Returns:
            Transaction status
        """
        return self.http.get(
            f"{self.base_path}/transactions/uetr/{uetr}/status"
        )

    def get_transaction_status_by_e2e(self, end_to_end_id: str) -> dict:
        """
        Get transaction status by end-to-end ID.

        Args:
            end_to_end_id: End-to-end transaction ID

        Returns:
            Transaction status
        """
        return self.http.get(
            f"{self.base_path}/transactions/e2e/{end_to_end_id}/status"
        )

    # Account Statement Operations

    def request_account_statement(self, data: dict) -> dict:
        """
        Request an account statement (camt.060).

        Args:
            data: Statement request data (account, fromDate, toDate, marketPractice)

        Returns:
            Statement request confirmation
        """
        return self.http.post(
            f"{self.base_path}/statements/request", json=data
        )

    def get_account_statement(self, statement_id: str) -> dict:
        """
        Get account statement by ID.

        Args:
            statement_id: Statement ID

        Returns:
            Account statement details
        """
        return self.http.get(f"{self.base_path}/statements/{statement_id}")

    def list_account_statements(
        self,
        account: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page: int = 1,
        limit: int = 20,
    ) -> dict:
        """
        List account statements.

        Args:
            account: Filter by account
            from_date: Filter from date
            to_date: Filter to date
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            List of account statements
        """
        params = {
            "account": account,
            "fromDate": from_date,
            "toDate": to_date,
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/statements", params=params)

    # Message Operations

    def list_messages(
        self,
        message_type: Optional[str] = None,
        status: Optional[str] = None,
        direction: Optional[str] = None,
        market_practice: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page: int = 1,
        limit: int = 20,
    ) -> dict:
        """
        List ISO 20022 messages.

        Args:
            message_type: Filter by message type
            status: Filter by status
            direction: Filter by direction (INBOUND, OUTBOUND)
            market_practice: Filter by market practice
            from_date: Filter from date
            to_date: Filter to date
            page: Page number (default: 1)
            limit: Items per page (default: 20)

        Returns:
            List of ISO 20022 messages
        """
        params = {
            "messageType": message_type,
            "status": status,
            "direction": direction,
            "marketPractice": market_practice,
            "fromDate": from_date,
            "toDate": to_date,
            "page": page,
            "limit": limit,
        }
        return self.http.get(f"{self.base_path}/messages", params=params)

    def get_message(self, message_id: str) -> dict:
        """
        Get message by ID.

        Args:
            message_id: Message ID

        Returns:
            ISO 20022 message details
        """
        return self.http.get(f"{self.base_path}/messages/{message_id}")

    def get_message_xml(self, message_id: str) -> str:
        """
        Get raw XML for a message.

        Args:
            message_id: Message ID

        Returns:
            XML string
        """
        return self.http.get(f"{self.base_path}/messages/{message_id}/xml")

    def reprocess_message(self, message_id: str) -> dict:
        """
        Reprocess a failed message.

        Args:
            message_id: Message ID

        Returns:
            Reprocessed message
        """
        return self.http.post(
            f"{self.base_path}/messages/{message_id}/reprocess"
        )

    # Validation Operations

    def validate_message(self, data: dict) -> dict:
        """
        Validate an ISO 20022 message.

        Args:
            data: Validation input (messageType, xml/json, marketPractice)

        Returns:
            Validation result
        """
        return self.http.post(f"{self.base_path}/validate", json=data)

    def validate_market_practice(
        self, message_id: str, practice: str
    ) -> dict:
        """
        Validate a message against a specific market practice.

        Args:
            message_id: Message ID
            practice: Market practice code

        Returns:
            Validation result
        """
        return self.http.post(
            f"{self.base_path}/messages/{message_id}/validate/{practice}"
        )

    # Market Practice Operations

    def list_market_practices(self) -> list:
        """
        Get supported market practices.

        Returns:
            List of market practice configurations
        """
        return self.http.get(f"{self.base_path}/market-practices")

    def get_market_practice_config(self, practice: str) -> dict:
        """
        Get market practice configuration.

        Args:
            practice: Market practice code (CBPR+, GCC, SEPA, etc.)

        Returns:
            Market practice configuration
        """
        return self.http.get(f"{self.base_path}/market-practices/{practice}")

    # Islamic Finance Operations

    def create_islamic_credit_transfer(self, data: dict) -> dict:
        """
        Create an Islamic finance credit transfer with Shariah compliance.

        Args:
            data: Credit transfer data with Islamic finance fields
                (contractType, shariahBoardRef, profitRate)

        Returns:
            Created message with validation result
        """
        data["islamicFinanceEnabled"] = True
        return self.http.post(
            f"{self.base_path}/islamic/credit-transfers", json=data
        )

    def get_islamic_purpose_codes(
        self, practice: Optional[str] = None
    ) -> list:
        """
        Get Islamic finance purpose codes for a market practice.

        Args:
            practice: Optional market practice filter

        Returns:
            List of purpose codes
        """
        params = {}
        if practice:
            params["practice"] = practice
        return self.http.get(
            f"{self.base_path}/islamic/purpose-codes", params=params
        )

    # Utility Operations

    def generate_uetr(self) -> dict:
        """
        Generate a UETR (Universal End-to-End Transaction Reference).

        Returns:
            Generated UETR
        """
        return self.http.post(f"{self.base_path}/utils/generate-uetr")

    def parse_xml(self, xml: str) -> dict:
        """
        Parse ISO 20022 XML to JSON.

        Args:
            xml: XML string

        Returns:
            Parsed message type and data
        """
        return self.http.post(
            f"{self.base_path}/utils/parse-xml", json={"xml": xml}
        )

    def to_xml(
        self,
        message_type: str,
        data: Any,
        market_practice: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict:
        """
        Convert JSON to ISO 20022 XML.

        Args:
            message_type: ISO 20022 message type
            data: Message data
            market_practice: Optional market practice
            version: Optional version

        Returns:
            XML string
        """
        payload: dict = {"messageType": message_type, "data": data}
        if market_practice:
            payload["marketPractice"] = market_practice
        if version:
            payload["version"] = version
        return self.http.post(f"{self.base_path}/utils/to-xml", json=payload)

    def get_supported_message_types(self) -> dict:
        """
        Get supported ISO 20022 message types.

        Returns:
            List of supported message types
        """
        return self.http.get(f"{self.base_path}/message-types")
