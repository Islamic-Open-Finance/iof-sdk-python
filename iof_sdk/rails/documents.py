"""Documents Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class DocumentsRail:
    """
    Documents Rail API client.

    Provides document management capabilities:
    - Document CRUD with upload/download URLs
    - Document verification
    - Shariah review
    - Document search
    - Document types
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Documents rail client."""
        self.http = http_client
        self.base_path = "/api/v1/documents"

    def list_documents(
        self,
        page: int = 1,
        limit: int = 20,
        document_type: Optional[str] = None,
        status: Optional[str] = None,
        contract_id: Optional[str] = None,
        customer_id: Optional[str] = None,
        case_id: Optional[str] = None,
        jurisdiction_code: Optional[str] = None,
        tag: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List documents with optional filters.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            document_type: Filter by document type
            status: Filter by status
            contract_id: Filter by contract ID
            customer_id: Filter by customer ID
            case_id: Filter by case ID
            jurisdiction_code: Filter by jurisdiction
            tag: Filter by tag

        Returns:
            Paginated list of documents
        """
        params = {
            "page": page,
            "limit": limit,
            "documentType": document_type,
            "status": status,
            "contractId": contract_id,
            "customerId": customer_id,
            "caseId": case_id,
            "jurisdictionCode": jurisdiction_code,
            "tag": tag,
        }
        return self.http.get(self.base_path, params=params)

    def create_document(self, data: dict) -> dict:
        """
        Create a new document and get upload URL.

        Args:
            data: Document creation data (name, documentType, mimeType, sizeBytes)

        Returns:
            Created document with upload URL
        """
        return self.http.post(self.base_path, json=data)

    def get_document(self, document_id: str) -> dict:
        """
        Get document by ID.

        Args:
            document_id: Document ID

        Returns:
            Document details
        """
        return self.http.get(f"{self.base_path}/{document_id}")

    def update_document(self, document_id: str, data: dict) -> dict:
        """
        Update document metadata.

        Args:
            document_id: Document ID
            data: Update data

        Returns:
            Updated document
        """
        return self.http.patch(f"{self.base_path}/{document_id}", json=data)

    def delete_document(self, document_id: str) -> None:
        """
        Delete a document.

        Args:
            document_id: Document ID
        """
        self.http.delete(f"{self.base_path}/{document_id}")

    def get_download_url(self, document_id: str) -> dict:
        """
        Get download URL for a document.

        Args:
            document_id: Document ID

        Returns:
            Download URL and expiration
        """
        return self.http.get(f"{self.base_path}/{document_id}/download-url")

    def confirm_upload(self, document_id: str) -> dict:
        """
        Confirm that a document upload is complete.

        Args:
            document_id: Document ID

        Returns:
            Updated document
        """
        return self.http.post(f"{self.base_path}/{document_id}/confirm-upload")

    def verify_document(self, document_id: str, verified: bool, notes: Optional[str] = None) -> dict:
        """
        Verify a document.

        Args:
            document_id: Document ID
            verified: Whether the document is verified
            notes: Optional verification notes

        Returns:
            Updated document
        """
        data = {"verified": verified, "notes": notes}
        return self.http.post(
            f"{self.base_path}/{document_id}/verify", json=data
        )

    def shariah_review(
        self,
        document_id: str,
        approved: bool,
        certificate_ref: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> dict:
        """
        Submit a Shariah review for a document.

        Args:
            document_id: Document ID
            approved: Whether the document is Shariah compliant
            certificate_ref: Optional certificate reference
            notes: Optional review notes

        Returns:
            Updated document
        """
        data = {
            "approved": approved,
            "certificateRef": certificate_ref,
            "notes": notes,
        }
        return self.http.post(
            f"{self.base_path}/{document_id}/shariah-review", json=data
        )

    def search_documents(self, data: dict) -> PaginatedResponse:
        """
        Search documents.

        Args:
            data: Search input (query, documentTypes, status, tags, etc.)

        Returns:
            Search results
        """
        return self.http.post(f"{self.base_path}/search", json=data)

    def get_document_types(self) -> list:
        """
        Get available document types.

        Returns:
            List of document type info
        """
        return self.http.get(f"{self.base_path}/types")
