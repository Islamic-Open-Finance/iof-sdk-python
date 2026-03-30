"""KYC Onboarding Rail API client."""

from typing import Any, Optional


class KycOnboardingRail:
    """
    KYC Onboarding Rail API client.

    Provides KYC application and onboarding workflows:
    - KYC application management
    - Document management
    - Identity verification
    - Compliance screening (AML, sanctions, PEP, Shariah)
    - Review and approval
    - Risk assessment
    - Beneficial owner management
    - Ongoing monitoring
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the KYC Onboarding rail client."""
        self.http = http_client
        self.base_path = "/v1/kyc"

    # KYC Applications

    def create_application(self, data: dict) -> dict:
        """
        Create a new KYC application.

        Args:
            data: Application data (userId, type, personalInfo, contactInfo)

        Returns:
            Created KYC application
        """
        return self.http.post(f"{self.base_path}/applications", json=data)

    def get_application(self, application_id: str) -> dict:
        """
        Get KYC application by ID.

        Args:
            application_id: Application ID

        Returns:
            KYC application details
        """
        return self.http.get(
            f"{self.base_path}/applications/{application_id}"
        )

    def update_application(self, application_id: str, data: dict) -> dict:
        """
        Update a KYC application.

        Args:
            application_id: Application ID
            data: Update data

        Returns:
            Updated KYC application
        """
        return self.http.patch(
            f"{self.base_path}/applications/{application_id}", json=data
        )

    def submit_application(self, application_id: str) -> dict:
        """
        Submit a KYC application for review.

        Args:
            application_id: Application ID

        Returns:
            Submitted application
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/submit"
        )

    def list_applications(
        self,
        user_id: Optional[str] = None,
        status: Optional[str] = None,
        application_type: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list:
        """
        List KYC applications.

        Args:
            user_id: Filter by user ID
            status: Filter by status
            application_type: Filter by application type
            limit: Items per page (default: 20)
            offset: Offset (default: 0)

        Returns:
            List of KYC applications
        """
        params = {
            "userId": user_id,
            "status": status,
            "type": application_type,
            "limit": limit,
            "offset": offset,
        }
        return self.http.get(f"{self.base_path}/applications", params=params)

    # Document Management

    def list_documents(self, application_id: str) -> list:
        """
        List documents for a KYC application.

        Args:
            application_id: Application ID

        Returns:
            List of documents
        """
        return self.http.get(
            f"{self.base_path}/applications/{application_id}/documents"
        )

    def delete_document(
        self, application_id: str, document_id: str
    ) -> None:
        """
        Delete a document from a KYC application.

        Args:
            application_id: Application ID
            document_id: Document ID
        """
        self.http.delete(
            f"{self.base_path}/applications/{application_id}/documents/{document_id}"
        )

    # Identity Verification

    def start_identity_verification(self, data: dict) -> dict:
        """
        Start identity verification.

        Args:
            data: Verification data (userId, method, documentId)

        Returns:
            Identity verification details
        """
        return self.http.post(
            f"{self.base_path}/identity-verification", json=data
        )

    def get_identity_verification(self, verification_id: str) -> dict:
        """
        Get identity verification by ID.

        Args:
            verification_id: Verification ID

        Returns:
            Verification details
        """
        return self.http.get(
            f"{self.base_path}/identity-verification/{verification_id}"
        )

    # Compliance Screening

    def run_aml_screening(self, application_id: str) -> dict:
        """
        Run AML screening for a KYC application.

        Args:
            application_id: Application ID

        Returns:
            AML screening result
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/screening/aml"
        )

    def run_sanctions_screening(self, application_id: str) -> dict:
        """
        Run sanctions screening for a KYC application.

        Args:
            application_id: Application ID

        Returns:
            Sanctions screening result
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/screening/sanctions"
        )

    def run_pep_screening(self, application_id: str) -> dict:
        """
        Run PEP screening for a KYC application.

        Args:
            application_id: Application ID

        Returns:
            PEP screening result
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/screening/pep"
        )

    def run_shariah_compliance(self, application_id: str) -> dict:
        """
        Run Shariah compliance check for a KYC application.

        Args:
            application_id: Application ID

        Returns:
            Shariah compliance result
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/screening/shariah"
        )

    def run_full_screening(self, application_id: str) -> dict:
        """
        Run full compliance screening (AML, sanctions, PEP, Shariah).

        Args:
            application_id: Application ID

        Returns:
            Full screening results
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/screening/full"
        )

    # Review & Approval

    def review_application(self, application_id: str, review: dict) -> dict:
        """
        Review a KYC application.

        Args:
            application_id: Application ID
            review: Review data (action, notes, requiredDocuments, riskLevel)

        Returns:
            Updated application
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/review",
            json=review,
        )

    def add_review_note(self, application_id: str, note: str) -> dict:
        """
        Add a review note to an application.

        Args:
            application_id: Application ID
            note: Note text

        Returns:
            Updated application
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/notes",
            json={"note": note},
        )

    def get_review_history(self, application_id: str) -> list:
        """
        Get review history for an application.

        Args:
            application_id: Application ID

        Returns:
            List of review notes
        """
        return self.http.get(
            f"{self.base_path}/applications/{application_id}/review-history"
        )

    # Risk Assessment

    def calculate_risk_score(self, application_id: str) -> dict:
        """
        Calculate risk score for an application.

        Args:
            application_id: Application ID

        Returns:
            Risk score with level and factors
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/risk-assessment"
        )

    # Beneficial Owners

    def add_beneficial_owner(self, application_id: str, owner: dict) -> dict:
        """
        Add a beneficial owner to a business application.

        Args:
            application_id: Application ID
            owner: Beneficial owner data

        Returns:
            Created beneficial owner
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/beneficial-owners",
            json=owner,
        )

    def list_beneficial_owners(self, application_id: str) -> list:
        """
        List beneficial owners for a business application.

        Args:
            application_id: Application ID

        Returns:
            List of beneficial owners
        """
        return self.http.get(
            f"{self.base_path}/applications/{application_id}/beneficial-owners"
        )

    def add_director(self, application_id: str, director: dict) -> dict:
        """
        Add a director to a business application.

        Args:
            application_id: Application ID
            director: Director data

        Returns:
            Created director
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/directors",
            json=director,
        )

    # Ongoing Monitoring

    def schedule_review(self, application_id: str, review_date: str) -> dict:
        """
        Schedule a periodic review.

        Args:
            application_id: Application ID
            review_date: Review date (ISO format)

        Returns:
            Updated application
        """
        return self.http.post(
            f"{self.base_path}/applications/{application_id}/schedule-review",
            json={"reviewDate": review_date},
        )

    def list_pending_reviews(
        self,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        risk_level: Optional[str] = None,
    ) -> list:
        """
        List applications with pending reviews.

        Args:
            from_date: Filter from date
            to_date: Filter to date
            risk_level: Filter by risk level

        Returns:
            List of applications pending review
        """
        params = {
            "from": from_date,
            "to": to_date,
            "riskLevel": risk_level,
        }
        return self.http.get(
            f"{self.base_path}/pending-reviews", params=params
        )
