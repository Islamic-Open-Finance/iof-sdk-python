"""Consent & Privacy Rail API client."""

from typing import Any, Optional

from ..models import PaginatedResponse


class ConsentPrivacyRail:
    """
    Consent & Privacy Rail API client.

    Provides GDPR/PDPA compliance capabilities:
    - Data subject management
    - Consent management and tracking
    - Data Subject Access Requests (DSAR)
    - Privacy preference management
    - Data breach reporting
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Consent & Privacy rail client."""
        self.http = http_client
        self.base_path = "/api/v1/privacy"

    # Data Subjects

    def register_data_subject(self, data: dict) -> dict:
        """
        Register a new data subject.

        Args:
            data: Data subject registration data (type, email, jurisdiction, etc.)

        Returns:
            Registered data subject
        """
        return self.http.post(f"{self.base_path}/subjects", json=data)

    def get_data_subject(self, subject_id: str) -> dict:
        """
        Get data subject by ID.

        Args:
            subject_id: Data subject ID

        Returns:
            Data subject details
        """
        return self.http.get(f"{self.base_path}/subjects/{subject_id}")

    def get_data_subject_by_email(self, email: str) -> dict:
        """
        Get data subject by email address.

        Args:
            email: Email address

        Returns:
            Data subject details
        """
        return self.http.get(
            f"{self.base_path}/subjects/by-email", params={"email": email}
        )

    def verify_data_subject(self, subject_id: str, method: str) -> dict:
        """
        Verify a data subject's identity.

        Args:
            subject_id: Data subject ID
            method: Verification method

        Returns:
            Updated data subject
        """
        return self.http.post(
            f"{self.base_path}/subjects/{subject_id}/verify",
            json={"method": method},
        )

    # Consents

    def list_consents(
        self,
        page: int = 1,
        limit: int = 20,
        data_subject_id: Optional[str] = None,
        purpose: Optional[str] = None,
        status: Optional[str] = None,
    ) -> PaginatedResponse:
        """
        List consent records.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            data_subject_id: Filter by data subject ID
            purpose: Filter by consent purpose
            status: Filter by status

        Returns:
            Paginated list of consent records
        """
        params = {
            "page": page,
            "limit": limit,
            "dataSubjectId": data_subject_id,
            "purpose": purpose,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/consents", params=params)

    def grant_consent(self, data: dict) -> dict:
        """
        Grant consent for a data subject.

        Args:
            data: Consent grant data (dataSubjectId, purpose, legalBasis, etc.)

        Returns:
            Consent record and receipt
        """
        return self.http.post(f"{self.base_path}/consents", json=data)

    def get_consent(self, consent_id: str) -> dict:
        """
        Get consent record by ID.

        Args:
            consent_id: Consent ID

        Returns:
            Consent record details
        """
        return self.http.get(f"{self.base_path}/consents/{consent_id}")

    def withdraw_consent(
        self, consent_id: str, reason: Optional[str] = None
    ) -> dict:
        """
        Withdraw a consent.

        Args:
            consent_id: Consent ID
            reason: Withdrawal reason

        Returns:
            Updated consent record
        """
        data = {}
        if reason:
            data["reason"] = reason
        return self.http.post(
            f"{self.base_path}/consents/{consent_id}/withdraw", json=data
        )

    def get_consent_receipt(self, consent_id: str) -> dict:
        """
        Get consent receipt.

        Args:
            consent_id: Consent ID

        Returns:
            Consent receipt
        """
        return self.http.get(f"{self.base_path}/consents/{consent_id}/receipt")

    def check_consent(
        self,
        data_subject_id: str,
        purpose: str,
        data_categories: Optional[list] = None,
    ) -> dict:
        """
        Check if consent exists for a given purpose.

        Args:
            data_subject_id: Data subject ID
            purpose: Consent purpose
            data_categories: Optional data categories to check

        Returns:
            Consent check result
        """
        data = {"dataSubjectId": data_subject_id, "purpose": purpose}
        if data_categories:
            data["dataCategories"] = data_categories
        return self.http.post(f"{self.base_path}/consents/check", json=data)

    def get_consents_by_subject(self, data_subject_id: str) -> dict:
        """
        Get all consents for a data subject.

        Args:
            data_subject_id: Data subject ID

        Returns:
            List of consent records
        """
        return self.http.get(
            f"{self.base_path}/subjects/{data_subject_id}/consents"
        )

    # DSARs

    def list_dsars(
        self,
        page: int = 1,
        limit: int = 20,
        data_subject_id: Optional[str] = None,
        dsar_type: Optional[str] = None,
        status: Optional[str] = None,
        assigned_to: Optional[str] = None,
        overdue: Optional[bool] = None,
    ) -> PaginatedResponse:
        """
        List Data Subject Access Requests.

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20)
            data_subject_id: Filter by data subject ID
            dsar_type: Filter by DSAR type
            status: Filter by status
            assigned_to: Filter by assignee
            overdue: Filter overdue requests

        Returns:
            Paginated list of DSARs
        """
        params = {
            "page": page,
            "limit": limit,
            "dataSubjectId": data_subject_id,
            "type": dsar_type,
            "status": status,
            "assignedTo": assigned_to,
            "overdue": overdue,
        }
        return self.http.get(f"{self.base_path}/dsars", params=params)

    def submit_dsar(self, data: dict) -> dict:
        """
        Submit a Data Subject Access Request.

        Args:
            data: DSAR submission data

        Returns:
            Submitted DSAR
        """
        return self.http.post(f"{self.base_path}/dsars", json=data)

    def get_dsar(self, dsar_id: str) -> dict:
        """
        Get DSAR by ID.

        Args:
            dsar_id: DSAR ID

        Returns:
            DSAR details
        """
        return self.http.get(f"{self.base_path}/dsars/{dsar_id}")

    def verify_dsar(self, dsar_id: str, data: dict) -> dict:
        """
        Verify a DSAR requester identity.

        Args:
            dsar_id: DSAR ID
            data: Verification data

        Returns:
            Updated DSAR
        """
        return self.http.post(
            f"{self.base_path}/dsars/{dsar_id}/verify", json=data
        )

    def assign_dsar(self, dsar_id: str, assignee_id: str) -> dict:
        """
        Assign a DSAR to a handler.

        Args:
            dsar_id: DSAR ID
            assignee_id: Assignee user ID

        Returns:
            Updated DSAR
        """
        return self.http.post(
            f"{self.base_path}/dsars/{dsar_id}/assign",
            json={"assigneeId": assignee_id},
        )

    def complete_dsar(self, dsar_id: str, data: dict) -> dict:
        """
        Complete a DSAR.

        Args:
            dsar_id: DSAR ID
            data: Completion data (responseType, dataExport, etc.)

        Returns:
            Completed DSAR with response
        """
        return self.http.post(
            f"{self.base_path}/dsars/{dsar_id}/complete", json=data
        )

    def request_dsar_extension(
        self, dsar_id: str, reason: str, additional_days: int
    ) -> dict:
        """
        Request a DSAR deadline extension.

        Args:
            dsar_id: DSAR ID
            reason: Extension reason
            additional_days: Number of additional days

        Returns:
            Updated DSAR
        """
        return self.http.post(
            f"{self.base_path}/dsars/{dsar_id}/extend",
            json={"reason": reason, "additionalDays": additional_days},
        )

    def get_dsar_response(self, dsar_id: str) -> dict:
        """
        Get DSAR response data.

        Args:
            dsar_id: DSAR ID

        Returns:
            DSAR response
        """
        return self.http.get(f"{self.base_path}/dsars/{dsar_id}/response")

    def get_dsar_stats(self) -> dict:
        """
        Get DSAR statistics.

        Returns:
            DSAR statistics (total, by status, overdue, avg completion)
        """
        return self.http.get(f"{self.base_path}/dsars/stats")

    # Privacy Preferences

    def get_preferences(self, data_subject_id: str) -> dict:
        """
        Get privacy preferences for a data subject.

        Args:
            data_subject_id: Data subject ID

        Returns:
            Privacy preferences
        """
        return self.http.get(f"{self.base_path}/preferences/{data_subject_id}")

    def update_preferences(self, data_subject_id: str, data: dict) -> dict:
        """
        Update privacy preferences.

        Args:
            data_subject_id: Data subject ID
            data: Updated preferences

        Returns:
            Updated privacy preferences
        """
        return self.http.patch(
            f"{self.base_path}/preferences/{data_subject_id}", json=data
        )

    # Data Breaches

    def list_breaches(self) -> dict:
        """
        List data breaches.

        Returns:
            List of data breaches
        """
        return self.http.get(f"{self.base_path}/breaches")

    def report_breach(self, data: dict) -> dict:
        """
        Report a data breach.

        Args:
            data: Breach report data

        Returns:
            Reported breach
        """
        return self.http.post(f"{self.base_path}/breaches", json=data)

    def get_breach(self, breach_id: str) -> dict:
        """
        Get data breach by ID.

        Args:
            breach_id: Breach ID

        Returns:
            Breach details
        """
        return self.http.get(f"{self.base_path}/breaches/{breach_id}")

    def update_breach_status(
        self, breach_id: str, status: str, notes: Optional[str] = None
    ) -> dict:
        """
        Update data breach status.

        Args:
            breach_id: Breach ID
            status: New status
            notes: Optional notes

        Returns:
            Updated breach
        """
        data = {"status": status, "notes": notes}
        return self.http.patch(
            f"{self.base_path}/breaches/{breach_id}", json=data
        )

    def notify_authority(
        self,
        breach_id: str,
        authority: str,
        reference: Optional[str] = None,
    ) -> dict:
        """
        Notify a regulatory authority about a breach.

        Args:
            breach_id: Breach ID
            authority: Authority name
            reference: Optional reference number

        Returns:
            Updated breach
        """
        data = {"authority": authority, "reference": reference}
        return self.http.post(
            f"{self.base_path}/breaches/{breach_id}/notify-authority", json=data
        )

    def notify_subjects(self, breach_id: str, method: str) -> dict:
        """
        Notify affected data subjects about a breach.

        Args:
            breach_id: Breach ID
            method: Notification method (email, postal, both)

        Returns:
            Updated breach
        """
        return self.http.post(
            f"{self.base_path}/breaches/{breach_id}/notify-subjects",
            json={"method": method},
        )
