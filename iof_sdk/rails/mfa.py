"""Multi-Factor Authentication (MFA) Rail API client."""

from typing import Any


class MfaRail:
    """
    Multi-Factor Authentication Rail API client.

    Provides MFA enrollment and verification:
    - TOTP (Time-based One-Time Password)
    - SMS OTP
    - Email OTP
    - Backup codes
    - MFA method management
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the MFA rail client."""
        self.http = http_client
        self.base_path = "/api/v1/mfa"

    # TOTP

    def enroll_totp(self) -> dict:
        """
        Start TOTP enrollment.

        Returns:
            Enrollment details (enrollmentId, secret, qrCodeUrl, manualEntryCode)
        """
        return self.http.post(f"{self.base_path}/totp/enroll", json={})

    def verify_totp_enrollment(self, enrollment_id: str, code: str) -> dict:
        """
        Verify TOTP enrollment with a code.

        Args:
            enrollment_id: Enrollment ID
            code: TOTP code

        Returns:
            Success response
        """
        return self.http.post(
            f"{self.base_path}/totp/verify",
            json={"enrollmentId": enrollment_id, "code": code},
        )

    # SMS OTP

    def send_sms_otp(self, phone_number: str) -> dict:
        """
        Send an SMS OTP.

        Args:
            phone_number: Phone number

        Returns:
            Challenge details (challengeId, destination, expiresAt)
        """
        return self.http.post(
            f"{self.base_path}/sms/send",
            json={"phoneNumber": phone_number},
        )

    def verify_sms_otp(self, challenge_id: str, code: str) -> dict:
        """
        Verify an SMS OTP.

        Args:
            challenge_id: Challenge ID
            code: OTP code

        Returns:
            Success response
        """
        return self.http.post(
            f"{self.base_path}/sms/verify",
            json={"challengeId": challenge_id, "code": code},
        )

    # Email OTP

    def send_email_otp(self, email: str) -> dict:
        """
        Send an Email OTP.

        Args:
            email: Email address

        Returns:
            Challenge details (challengeId, destination, expiresAt)
        """
        return self.http.post(
            f"{self.base_path}/email/send", json={"email": email}
        )

    def verify_email_otp(self, challenge_id: str, code: str) -> dict:
        """
        Verify an Email OTP.

        Args:
            challenge_id: Challenge ID
            code: OTP code

        Returns:
            Success response
        """
        return self.http.post(
            f"{self.base_path}/email/verify",
            json={"challengeId": challenge_id, "code": code},
        )

    # Backup Codes

    def generate_backup_codes(self) -> dict:
        """
        Generate backup codes.

        Returns:
            Generated backup codes and message
        """
        return self.http.post(
            f"{self.base_path}/backup-codes/generate", json={}
        )

    def verify_backup_code(self, code: str) -> dict:
        """
        Verify a backup code.

        Args:
            code: Backup code

        Returns:
            Success response
        """
        return self.http.post(
            f"{self.base_path}/backup-codes/verify", json={"code": code}
        )

    # MFA Management

    def get_mfa_methods(self) -> dict:
        """
        Get enrolled MFA methods.

        Returns:
            List of MFA methods
        """
        return self.http.get(f"{self.base_path}/methods")

    def remove_mfa_method(self, method_id: str) -> dict:
        """
        Remove an MFA method.

        Args:
            method_id: Method ID

        Returns:
            Success response
        """
        return self.http.delete(f"{self.base_path}/methods/{method_id}")
