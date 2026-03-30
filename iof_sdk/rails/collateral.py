"""Collateral Management Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class CollateralRail:
    """
    Collateral Management Rail API client.

    Provides Shariah-compliant collateral management:
    - Collateral asset registration and verification
    - Lien management
    - Valuation tracking and approval
    - Coverage ratio monitoring
    - Collateral pools
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Collateral rail client."""
        self.http = http_client
        self.base_path = "/api/v1/collateral"

    # Collateral Assets

    def list_collateral(
        self,
        page: int = 1,
        limit: int = 20,
        asset_type: Optional[str] = None,
        status: Optional[str] = None,
        owner_id: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List collateral assets.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            asset_type: Filter by asset type
            status: Filter by status
            owner_id: Filter by owner ID

        Returns:
            Paginated list of collateral assets
        """
        params = {
            "page": page,
            "limit": limit,
            "type": asset_type,
            "status": status,
            "ownerId": owner_id,
        }
        return self.http.get(self.base_path, params=params)

    def register_collateral(self, data: dict) -> dict:
        """
        Register a new collateral asset.

        Args:
            data: Collateral registration data

        Returns:
            Registered collateral asset
        """
        return self.http.post(self.base_path, json=data)

    def get_collateral(self, collateral_id: str) -> dict:
        """
        Get collateral asset by ID.

        Args:
            collateral_id: Collateral ID

        Returns:
            Collateral asset details
        """
        return self.http.get(f"{self.base_path}/{collateral_id}")

    def update_collateral(self, collateral_id: str, data: dict) -> dict:
        """
        Update collateral asset.

        Args:
            collateral_id: Collateral ID
            data: Update data

        Returns:
            Updated collateral asset
        """
        return self.http.patch(f"{self.base_path}/{collateral_id}", json=data)

    def verify_collateral(self, collateral_id: str) -> dict:
        """
        Verify a collateral asset.

        Args:
            collateral_id: Collateral ID

        Returns:
            Verified collateral asset
        """
        return self.http.post(f"{self.base_path}/{collateral_id}/verify")

    # Liens

    def list_liens(
        self,
        page: int = 1,
        limit: int = 20,
        collateral_id: Optional[str] = None,
        contract_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List liens.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            collateral_id: Filter by collateral ID
            contract_id: Filter by contract ID
            status: Filter by status

        Returns:
            Paginated list of liens
        """
        params = {
            "page": page,
            "limit": limit,
            "collateralId": collateral_id,
            "contractId": contract_id,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/liens", params=params)

    def create_lien(self, data: dict) -> dict:
        """
        Create a new lien on collateral.

        Args:
            data: Lien creation data

        Returns:
            Created lien
        """
        return self.http.post(f"{self.base_path}/liens", json=data)

    def get_lien(self, lien_id: str) -> dict:
        """
        Get lien by ID.

        Args:
            lien_id: Lien ID

        Returns:
            Lien details
        """
        return self.http.get(f"{self.base_path}/liens/{lien_id}")

    def activate_lien(self, lien_id: str) -> dict:
        """
        Activate a lien.

        Args:
            lien_id: Lien ID

        Returns:
            Activated lien
        """
        return self.http.post(f"{self.base_path}/liens/{lien_id}/activate")

    def release_lien(self, lien_id: str, reason: str) -> dict:
        """
        Release a lien.

        Args:
            lien_id: Lien ID
            reason: Release reason

        Returns:
            Released lien
        """
        return self.http.post(
            f"{self.base_path}/liens/{lien_id}/release", json={"reason": reason}
        )

    # Valuations

    def list_valuations(
        self,
        page: int = 1,
        limit: int = 20,
        collateral_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List valuations.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            collateral_id: Filter by collateral ID
            status: Filter by status

        Returns:
            Paginated list of valuations
        """
        params = {
            "page": page,
            "limit": limit,
            "collateralId": collateral_id,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/valuations", params=params)

    def submit_valuation(self, data: dict) -> dict:
        """
        Submit a new valuation.

        Args:
            data: Valuation submission data

        Returns:
            Submitted valuation
        """
        return self.http.post(f"{self.base_path}/valuations", json=data)

    def get_valuation(self, valuation_id: str) -> dict:
        """
        Get valuation by ID.

        Args:
            valuation_id: Valuation ID

        Returns:
            Valuation details
        """
        return self.http.get(f"{self.base_path}/valuations/{valuation_id}")

    def approve_valuation(self, valuation_id: str, approved: bool, rejection_reason: Optional[str] = None) -> dict:
        """
        Approve or reject a valuation.

        Args:
            valuation_id: Valuation ID
            approved: Whether to approve
            rejection_reason: Reason for rejection (if not approved)

        Returns:
            Updated valuation
        """
        data = {"approved": approved, "rejectionReason": rejection_reason}
        return self.http.post(
            f"{self.base_path}/valuations/{valuation_id}/approve", json=data
        )

    # Coverage

    def get_coverage(self, contract_id: str) -> dict:
        """
        Get collateral coverage for a contract.

        Args:
            contract_id: Contract ID

        Returns:
            Collateral coverage details
        """
        return self.http.get(f"{self.base_path}/coverage/{contract_id}")

    def calculate_coverage(self, contract_id: str) -> dict:
        """
        Calculate collateral coverage for a contract.

        Args:
            contract_id: Contract ID

        Returns:
            Calculated coverage details
        """
        return self.http.post(f"{self.base_path}/coverage/{contract_id}/calculate")

    # Pools

    def list_pools(self) -> dict:
        """
        List collateral pools.

        Returns:
            List of collateral pools
        """
        return self.http.get(f"{self.base_path}/pools")

    def create_pool(self, data: dict) -> dict:
        """
        Create a collateral pool.

        Args:
            data: Pool creation data

        Returns:
            Created pool
        """
        return self.http.post(f"{self.base_path}/pools", json=data)

    def get_pool(self, pool_id: str) -> dict:
        """
        Get collateral pool by ID.

        Args:
            pool_id: Pool ID

        Returns:
            Pool details
        """
        return self.http.get(f"{self.base_path}/pools/{pool_id}")

    def add_to_pool(self, pool_id: str, collateral_id: str) -> None:
        """
        Add collateral to a pool.

        Args:
            pool_id: Pool ID
            collateral_id: Collateral ID to add
        """
        self.http.post(
            f"{self.base_path}/pools/{pool_id}/members",
            json={"collateralId": collateral_id},
        )

    def remove_from_pool(self, pool_id: str, collateral_id: str) -> None:
        """
        Remove collateral from a pool.

        Args:
            pool_id: Pool ID
            collateral_id: Collateral ID to remove
        """
        self.http.delete(f"{self.base_path}/pools/{pool_id}/members/{collateral_id}")
