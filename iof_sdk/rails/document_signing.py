"""Document Signing Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class DocumentSigningRail:
    """
    Document Signing Rail API client.

    Provides document signing capabilities:
    - Signing request management
    - Multi-party signature workflows
    - Signature fields
    - Signing certificates
    - Templates
    - E-seal management
    - Audit trail
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Document Signing rail client."""
        self.http = http_client
        self.base_path = "/api/v1/signing"

    # Signing Requests

    def list_requests(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
        contract_id: Optional[str] = None,
        document_id: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List signing requests.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status
            contract_id: Filter by contract ID
            document_id: Filter by document ID

        Returns:
            Paginated list of signing requests
        """
        params = {
            "page": page,
            "limit": limit,
            "status": status,
            "contractId": contract_id,
            "documentId": document_id,
        }
        return self.http.get(f"{self.base_path}/requests", params=params)

    def create_request(self, data: dict) -> dict:
        """
        Create a new signing request.

        Args:
            data: Signing request data (documentId, signers, fields, etc.)

        Returns:
            Created signing request
        """
        return self.http.post(f"{self.base_path}/requests", json=data)

    def get_request(self, request_id: str) -> dict:
        """
        Get signing request by ID.

        Args:
            request_id: Request ID

        Returns:
            Signing request details
        """
        return self.http.get(f"{self.base_path}/requests/{request_id}")

    def send_request(self, request_id: str) -> dict:
        """
        Send a signing request to signers.

        Args:
            request_id: Request ID

        Returns:
            Updated signing request
        """
        return self.http.post(f"{self.base_path}/requests/{request_id}/send")

    def void_request(
        self,
        request_id: str,
        reason: str,
        notify_signers: bool = True,
    ) -> dict:
        """
        Void a signing request.

        Args:
            request_id: Request ID
            reason: Void reason
            notify_signers: Whether to notify signers

        Returns:
            Voided signing request
        """
        return self.http.post(
            f"{self.base_path}/requests/{request_id}/void",
            json={"reason": reason, "notifySigners": notify_signers},
        )

    def get_requests_by_contract(self, contract_id: str) -> dict:
        """
        Get signing requests for a contract.

        Args:
            contract_id: Contract ID

        Returns:
            List of signing requests
        """
        return self.http.get(
            f"{self.base_path}/contracts/{contract_id}/requests"
        )

    # Signer Actions

    def record_view(self, request_id: str, signer_id: str) -> dict:
        """
        Record that a signer viewed the document.

        Args:
            request_id: Request ID
            signer_id: Signer ID

        Returns:
            Updated signing request
        """
        return self.http.post(
            f"{self.base_path}/requests/{request_id}/signers/{signer_id}/view"
        )

    def record_signature(
        self, request_id: str, signer_id: str, data: Optional[dict] = None
    ) -> dict:
        """
        Record a signature.

        Args:
            request_id: Request ID
            signer_id: Signer ID
            data: Optional signature metadata (ipAddress, userAgent, geolocation)

        Returns:
            Updated signing request
        """
        return self.http.post(
            f"{self.base_path}/requests/{request_id}/signers/{signer_id}/sign",
            json=data or {},
        )

    def decline_signature(
        self, request_id: str, signer_id: str, reason: str
    ) -> dict:
        """
        Decline to sign.

        Args:
            request_id: Request ID
            signer_id: Signer ID
            reason: Decline reason

        Returns:
            Updated signing request
        """
        return self.http.post(
            f"{self.base_path}/requests/{request_id}/signers/{signer_id}/decline",
            json={"reason": reason},
        )

    def send_reminder(self, request_id: str, signer_id: str) -> None:
        """
        Send a signing reminder to a signer.

        Args:
            request_id: Request ID
            signer_id: Signer ID
        """
        self.http.post(
            f"{self.base_path}/requests/{request_id}/signers/{signer_id}/remind"
        )

    # Fields

    def get_fields(self, request_id: str) -> dict:
        """
        Get signature fields for a request.

        Args:
            request_id: Request ID

        Returns:
            List of signature fields
        """
        return self.http.get(f"{self.base_path}/requests/{request_id}/fields")

    def fill_field(self, request_id: str, field_id: str, value: str) -> dict:
        """
        Fill a signature field.

        Args:
            request_id: Request ID
            field_id: Field ID
            value: Field value

        Returns:
            Updated field
        """
        return self.http.patch(
            f"{self.base_path}/requests/{request_id}/fields/{field_id}",
            json={"value": value},
        )

    # Certificates

    def get_certificate(self, request_id: str) -> dict:
        """
        Get signing certificate for a completed request.

        Args:
            request_id: Request ID

        Returns:
            Signature certificate
        """
        return self.http.get(
            f"{self.base_path}/requests/{request_id}/certificate"
        )

    def verify_certificate(self, certificate_number: str) -> dict:
        """
        Verify a signing certificate.

        Args:
            certificate_number: Certificate number

        Returns:
            Verification result
        """
        return self.http.get(
            f"{self.base_path}/certificates/verify/{certificate_number}"
        )

    # Templates

    def list_templates(
        self,
        page: int = 1,
        limit: int = 20,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List signing templates.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            status: Filter by status (draft, active, archived)

        Returns:
            Paginated list of templates
        """
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(f"{self.base_path}/templates", params=params)

    def create_template(self, data: dict) -> dict:
        """
        Create a signing template.

        Args:
            data: Template data

        Returns:
            Created template
        """
        return self.http.post(f"{self.base_path}/templates", json=data)

    def get_template(self, template_id: str) -> dict:
        """
        Get template by ID.

        Args:
            template_id: Template ID

        Returns:
            Template details
        """
        return self.http.get(f"{self.base_path}/templates/{template_id}")

    def update_template(self, template_id: str, data: dict) -> dict:
        """
        Update a template.

        Args:
            template_id: Template ID
            data: Update data

        Returns:
            Updated template
        """
        return self.http.patch(
            f"{self.base_path}/templates/{template_id}", json=data
        )

    def archive_template(self, template_id: str) -> dict:
        """
        Archive a template.

        Args:
            template_id: Template ID

        Returns:
            Archived template
        """
        return self.http.post(
            f"{self.base_path}/templates/{template_id}/archive"
        )

    def create_request_from_template(
        self,
        template_id: str,
        signers: list,
        document_id: Optional[str] = None,
    ) -> dict:
        """
        Create a signing request from a template.

        Args:
            template_id: Template ID
            signers: List of signer data
            document_id: Optional document ID override

        Returns:
            Created signing request
        """
        data: dict = {"signers": signers}
        if document_id:
            data["documentId"] = document_id
        return self.http.post(
            f"{self.base_path}/templates/{template_id}/create-request",
            json=data,
        )

    # E-Seals

    def list_eseal_configs(self) -> dict:
        """
        List e-seal configurations.

        Returns:
            List of e-seal configs
        """
        return self.http.get(f"{self.base_path}/eseals")

    def create_eseal_config(self, data: dict) -> dict:
        """
        Create an e-seal configuration.

        Args:
            data: E-seal config data

        Returns:
            Created e-seal config
        """
        return self.http.post(f"{self.base_path}/eseals", json=data)

    def get_eseal_config(self, eseal_id: str) -> dict:
        """
        Get e-seal config by ID.

        Args:
            eseal_id: E-seal config ID

        Returns:
            E-seal config details
        """
        return self.http.get(f"{self.base_path}/eseals/{eseal_id}")

    def update_eseal_config(self, eseal_id: str, data: dict) -> dict:
        """
        Update an e-seal configuration.

        Args:
            eseal_id: E-seal config ID
            data: Update data

        Returns:
            Updated e-seal config
        """
        return self.http.patch(
            f"{self.base_path}/eseals/{eseal_id}", json=data
        )

    def suspend_eseal(self, eseal_id: str) -> dict:
        """
        Suspend an e-seal.

        Args:
            eseal_id: E-seal config ID

        Returns:
            Suspended e-seal config
        """
        return self.http.post(f"{self.base_path}/eseals/{eseal_id}/suspend")

    def activate_eseal(self, eseal_id: str) -> dict:
        """
        Activate an e-seal.

        Args:
            eseal_id: E-seal config ID

        Returns:
            Activated e-seal config
        """
        return self.http.post(f"{self.base_path}/eseals/{eseal_id}/activate")

    def apply_eseal(self, data: dict) -> dict:
        """
        Apply an e-seal to a document.

        Args:
            data: E-seal application data

        Returns:
            E-seal application result
        """
        return self.http.post(f"{self.base_path}/eseals/apply", json=data)

    def approve_eseal_application(self, application_id: str) -> dict:
        """
        Approve an e-seal application.

        Args:
            application_id: Application ID

        Returns:
            Approved application
        """
        return self.http.post(
            f"{self.base_path}/eseal-applications/{application_id}/approve"
        )

    def reject_eseal_application(
        self, application_id: str, reason: str
    ) -> dict:
        """
        Reject an e-seal application.

        Args:
            application_id: Application ID
            reason: Rejection reason

        Returns:
            Rejected application
        """
        return self.http.post(
            f"{self.base_path}/eseal-applications/{application_id}/reject",
            json={"reason": reason},
        )

    # Audit Trail

    def get_audit_trail(self, request_id: str) -> dict:
        """
        Get signing audit trail for a request.

        Args:
            request_id: Request ID

        Returns:
            List of audit trail entries
        """
        return self.http.get(
            f"{self.base_path}/requests/{request_id}/audit-trail"
        )
