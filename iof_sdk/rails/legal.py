"""Legal & Documentation Rail API client."""

from typing import Any, Optional

from ..models import LegalDocument, PaginatedResponse


class LegalRail:
    """
    Legal & Documentation Rail API client.

    Handles legal template and document management.
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Legal rail client."""
        self.http = http_client
        self.base_path = "/api/v1/legal"

    # Documents
    def list_documents(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List legal documents.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by document type
            status: Filter by status

        Returns:
            Paginated list of legal documents
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/documents", params=params)

    def get_document(self, document_id: str) -> LegalDocument:
        """
        Get legal document by ID.

        Args:
            document_id: Document ID

        Returns:
            Legal document details
        """
        return self.http.get(f"{self.base_path}/documents/{document_id}")

    def create_document(self, data: dict) -> LegalDocument:
        """
        Create a new legal document.

        Args:
            data: Document creation data

        Returns:
            Created legal document
        """
        return self.http.post(f"{self.base_path}/documents", json=data)

    def update_document(self, document_id: str, data: dict) -> LegalDocument:
        """
        Update a legal document.

        Args:
            document_id: Document ID
            data: Document update data

        Returns:
            Updated legal document
        """
        return self.http.patch(f"{self.base_path}/documents/{document_id}", json=data)

    # Templates
    def list_templates(
        self,
        page: int = 1,
        limit: int = 20,
        type: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List legal templates.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            type: Filter by template type

        Returns:
            Paginated list of legal templates
        """
        params = {
            "page": page,
            "limit": limit,
            "type": type,
        }
        return self.http.get(f"{self.base_path}/templates", params=params)

    def get_template(self, template_id: str) -> dict:
        """
        Get legal template by ID.

        Args:
            template_id: Template ID

        Returns:
            Legal template details
        """
        return self.http.get(f"{self.base_path}/templates/{template_id}")

    def generate_from_template(self, template_id: str, data: dict) -> LegalDocument:
        """
        Generate a document from a template.

        Args:
            template_id: Template ID
            data: Template variables

        Returns:
            Generated legal document
        """
        return self.http.post(
            f"{self.base_path}/templates/{template_id}/generate", json=data
        )

    # Signing
    def sign_document(self, document_id: str, signature_data: dict) -> LegalDocument:
        """
        Sign a legal document.

        Args:
            document_id: Document ID
            signature_data: Signature information

        Returns:
            Signed document
        """
        return self.http.post(
            f"{self.base_path}/documents/{document_id}/sign", json=signature_data
        )

    def get_document_signers(self, document_id: str) -> list:
        """
        Get document signers.

        Args:
            document_id: Document ID

        Returns:
            List of signers
        """
        return self.http.get(f"{self.base_path}/documents/{document_id}/signers")
