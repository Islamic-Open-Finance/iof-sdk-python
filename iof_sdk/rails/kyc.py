"""KYC & Screening Rail API client."""

from typing import Any, Optional

from ..models import CreateCustomerRequest, Customer, PaginatedResponse, ScreeningResult


class KycRail:
    """
    KYC & Screening Rail API client.

    Handles customer verification, identity verification,
    and screening operations.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the KYC rail client."""
        self.http = http_client
        self.base_path = "/api/v1/kyc"

    def list_customers(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List customers with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            type: Filter by type (individual/corporate)

        Returns:
            Paginated list of customers
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
        }
        return self.http.get(f"{self.base_path}/customers", params=params)

    def get_customer(self, customer_id: str) -> Customer:
        """
        Get customer by ID.

        Args:
            customer_id: Customer ID

        Returns:
            Customer details
        """
        return self.http.get(f"{self.base_path}/customers/{customer_id}")

    def create_customer(self, data: CreateCustomerRequest) -> Customer:
        """
        Create a new customer.

        Args:
            data: Customer creation data

        Returns:
            Created customer
        """
        return self.http.post(f"{self.base_path}/customers", json=data)

    def update_customer(self, customer_id: str, data: dict) -> Customer:
        """
        Update customer information.

        Args:
            customer_id: Customer ID
            data: Customer update data

        Returns:
            Updated customer
        """
        return self.http.patch(f"{self.base_path}/customers/{customer_id}", json=data)

    def verify_customer(self, customer_id: str) -> Customer:
        """
        Verify a customer.

        Args:
            customer_id: Customer ID

        Returns:
            Verified customer
        """
        return self.http.post(f"{self.base_path}/customers/{customer_id}/verify")

    def screen_customer(self, customer_id: str) -> ScreeningResult:
        """
        Screen a customer against watchlists.

        Args:
            customer_id: Customer ID

        Returns:
            Screening result
        """
        return self.http.post(f"{self.base_path}/customers/{customer_id}/screen")

    def get_customer_documents(self, customer_id: str) -> list:
        """
        Get customer documents.

        Args:
            customer_id: Customer ID

        Returns:
            List of customer documents
        """
        return self.http.get(f"{self.base_path}/customers/{customer_id}/documents")
