"""Partner & Embedded Finance Rail API client."""

from typing import Any, Optional

from ..models import Partner, PaginatedResponse, Program


class PartnersRail:
    """
    Partner & Embedded Finance Rail API client.

    Handles partner programs, revenue sharing, and embedded finance
    marketplace management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Partners rail client."""
        self.http = http_client
        self.base_path = "/api/v1/partners"

    # Partners
    def list_partners(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List partners.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            type: Filter by partner type

        Returns:
            Paginated list of partners
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "type": type,
        }
        return self.http.get(self.base_path, params=params)

    def get_partner(self, partner_id: str) -> Partner:
        """
        Get partner by ID.

        Args:
            partner_id: Partner ID

        Returns:
            Partner details
        """
        return self.http.get(f"{self.base_path}/{partner_id}")

    def create_partner(self, data: dict) -> Partner:
        """
        Create a new partner.

        Args:
            data: Partner creation data

        Returns:
            Created partner
        """
        return self.http.post(self.base_path, json=data)

    def update_partner(self, partner_id: str, data: dict) -> Partner:
        """
        Update a partner.

        Args:
            partner_id: Partner ID
            data: Partner update data

        Returns:
            Updated partner
        """
        return self.http.patch(f"{self.base_path}/{partner_id}", json=data)

    # Programs
    def list_programs(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List partner programs.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status

        Returns:
            Paginated list of programs
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/programs", params=params)

    def get_program(self, program_id: str) -> Program:
        """
        Get program by ID.

        Args:
            program_id: Program ID

        Returns:
            Program details
        """
        return self.http.get(f"{self.base_path}/programs/{program_id}")

    def create_program(self, data: dict) -> Program:
        """
        Create a new partner program.

        Args:
            data: Program creation data

        Returns:
            Created program
        """
        return self.http.post(f"{self.base_path}/programs", json=data)

    def update_program(self, program_id: str, data: dict) -> Program:
        """
        Update a partner program.

        Args:
            program_id: Program ID
            data: Program update data

        Returns:
            Updated program
        """
        return self.http.patch(f"{self.base_path}/programs/{program_id}", json=data)

    # Revenue Sharing
    def get_revenue_report(
        self,
        partner_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get partner revenue report.

        Args:
            partner_id: Partner ID
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            Revenue report
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(
            f"{self.base_path}/{partner_id}/revenue", params=params
        )

    def get_commission_report(
        self,
        partner_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        """
        Get partner commission report.

        Args:
            partner_id: Partner ID
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            Commission report
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.http.get(
            f"{self.base_path}/{partner_id}/commissions", params=params
        )
