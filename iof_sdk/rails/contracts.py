"""Contracts Rail API client."""

from typing import Any, Dict, List, Optional

from ..models import Contract, CreateContractRequest, PaginatedResponse, UpdateContractRequest, ValidationResult


class ContractsRail:
    """
    Contracts Rail API client.

    Handles Islamic finance contract lifecycle management including
    creation, execution, termination, and validation.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Contracts rail client."""
        self.http = http_client
        self.base_path = "/api/v1/contracts"

    def list_contracts(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
        currency: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List contracts with optional filtering.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status (e.g., "ACTIVE", "TERMINATED")
            type: Filter by contract type (e.g., "MURABAHA", "IJARA")
            currency: Filter by currency

        Returns:
            Paginated list of contracts
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
            "currency": currency,
        }
        return self.http.get(self.base_path, params=params)

    def get_contract(self, contract_id: str) -> Contract:
        """
        Get contract by ID.

        Args:
            contract_id: Contract ID

        Returns:
            Contract details
        """
        return self.http.get(f"{self.base_path}/{contract_id}")

    def create_contract(self, data: CreateContractRequest) -> Contract:
        """
        Create a new contract.

        Args:
            data: Contract creation data

        Returns:
            Created contract
        """
        return self.http.post(self.base_path, json=data)

    def update_contract(
        self, contract_id: str, data: UpdateContractRequest
    ) -> Contract:
        """
        Update an existing contract.

        Args:
            contract_id: Contract ID
            data: Contract update data

        Returns:
            Updated contract
        """
        return self.http.patch(f"{self.base_path}/{contract_id}", json=data)

    def execute_contract(self, contract_id: str) -> Contract:
        """
        Execute a contract.

        Args:
            contract_id: Contract ID

        Returns:
            Executed contract
        """
        return self.http.post(f"{self.base_path}/{contract_id}/execute")

    def terminate_contract(self, contract_id: str, reason: str) -> Contract:
        """
        Terminate a contract.

        Args:
            contract_id: Contract ID
            reason: Termination reason

        Returns:
            Terminated contract
        """
        return self.http.post(
            f"{self.base_path}/{contract_id}/terminate", json={"reason": reason}
        )

    def validate_contract(self, data: CreateContractRequest) -> ValidationResult:
        """
        Validate contract data without creating it.

        Args:
            data: Contract data to validate

        Returns:
            Validation result
        """
        return self.http.post(f"{self.base_path}/validate", json=data)

    def get_contract_history(self, contract_id: str) -> List[Dict[str, Any]]:
        """
        Get contract audit history.

        Args:
            contract_id: Contract ID

        Returns:
            List of audit log entries
        """
        return self.http.get(f"{self.base_path}/{contract_id}/history")

    def get_contract_documents(self, contract_id: str) -> List[Dict[str, Any]]:
        """
        Get contract documents.

        Args:
            contract_id: Contract ID

        Returns:
            List of contract documents
        """
        return self.http.get(f"{self.base_path}/{contract_id}/documents")
