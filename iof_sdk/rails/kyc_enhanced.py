"""KYC Enhanced Rail API client."""

from typing import Any, Optional


class KycEnhancedRail:
    """
    KYC Enhanced Rail API client.

    Provides Know Your Customer capabilities:
    - Subject management (individuals and businesses)
    - KYC profiles and risk assessment
    - Verification workflows
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the KYC Enhanced rail client."""
        self.http = http_client
        self.base_path = "/api/v1/kyc"

    # KYC Subjects

    def list_subjects(
        self,
        subject_type: Optional[str] = None,
        kyc_status: Optional[str] = None,
        risk_band: Optional[str] = None,
        country: Optional[str] = None,
        pep: Optional[bool] = None,
        sanctioned: Optional[bool] = None,
    ) -> dict:
        """
        List KYC subjects.

        Args:
            subject_type: Filter by type (INDIVIDUAL, BUSINESS)
            kyc_status: Filter by KYC status
            risk_band: Filter by risk band
            country: Filter by country
            pep: Filter by PEP status
            sanctioned: Filter by sanctions status

        Returns:
            List of KYC subjects with count
        """
        params = {
            "subjectType": subject_type,
            "kycStatus": kyc_status,
            "riskBand": risk_band,
            "country": country,
            "pep": pep,
            "sanctioned": sanctioned,
        }
        return self.http.get(f"{self.base_path}/subjects", params=params)

    def create_subject(self, data: dict) -> dict:
        """
        Create a new KYC subject.

        Args:
            data: Subject data (subjectType, fullName, country, etc.)

        Returns:
            Created KYC subject
        """
        return self.http.post(f"{self.base_path}/subjects", json=data)

    def get_subject(self, subject_id: str) -> dict:
        """
        Get KYC subject by ID.

        Args:
            subject_id: Subject ID

        Returns:
            KYC subject details
        """
        return self.http.get(f"{self.base_path}/subjects/{subject_id}")

    def update_subject(self, subject_id: str, data: dict) -> dict:
        """
        Update a KYC subject.

        Args:
            subject_id: Subject ID
            data: Update data

        Returns:
            Updated KYC subject
        """
        return self.http.patch(
            f"{self.base_path}/subjects/{subject_id}", json=data
        )

    # KYC Profiles

    def list_profiles(
        self,
        kyc_status: Optional[str] = None,
        risk_band: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
    ) -> dict:
        """
        List KYC profiles.

        Args:
            kyc_status: Filter by KYC status
            risk_band: Filter by risk band
            jurisdiction_id: Filter by jurisdiction ID

        Returns:
            List of KYC profiles with count
        """
        params = {
            "kycStatus": kyc_status,
            "riskBand": risk_band,
            "jurisdictionId": jurisdiction_id,
        }
        return self.http.get(f"{self.base_path}/profiles", params=params)

    def create_profile(self, data: dict) -> dict:
        """
        Create a new KYC profile.

        Args:
            data: Profile data (subjectId, jurisdictionId, riskBand, etc.)

        Returns:
            Created KYC profile
        """
        return self.http.post(f"{self.base_path}/profiles", json=data)

    def get_profile(self, profile_id: str) -> dict:
        """
        Get KYC profile by ID.

        Args:
            profile_id: Profile ID

        Returns:
            KYC profile details
        """
        return self.http.get(f"{self.base_path}/profiles/{profile_id}")

    def update_profile(self, profile_id: str, data: dict) -> dict:
        """
        Update a KYC profile (approve, reject, etc.).

        Args:
            profile_id: Profile ID
            data: Update data

        Returns:
            Updated KYC profile
        """
        return self.http.patch(
            f"{self.base_path}/profiles/{profile_id}", json=data
        )

    # KYC Verifications

    def list_verifications(
        self,
        subject_id: Optional[str] = None,
        verification_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> dict:
        """
        List KYC verifications.

        Args:
            subject_id: Filter by subject ID
            verification_type: Filter by type (DOCUMENT, BIOMETRIC, etc.)
            status: Filter by status

        Returns:
            List of KYC verifications with count
        """
        params = {
            "subjectId": subject_id,
            "verificationType": verification_type,
            "status": status,
        }
        return self.http.get(f"{self.base_path}/verifications", params=params)

    def create_verification(self, data: dict) -> dict:
        """
        Initiate a new KYC verification.

        Args:
            data: Verification data (subjectId, verificationType, etc.)

        Returns:
            Created verification
        """
        return self.http.post(f"{self.base_path}/verifications", json=data)

    def get_verification(self, verification_id: str) -> dict:
        """
        Get KYC verification by ID.

        Args:
            verification_id: Verification ID

        Returns:
            Verification details
        """
        return self.http.get(
            f"{self.base_path}/verifications/{verification_id}"
        )

    def update_verification(self, verification_id: str, data: dict) -> dict:
        """
        Update verification status (mark as verified/failed).

        Args:
            verification_id: Verification ID
            data: Update data (status, verifiedBy, rejectionReason)

        Returns:
            Updated verification
        """
        return self.http.patch(
            f"{self.base_path}/verifications/{verification_id}", json=data
        )
