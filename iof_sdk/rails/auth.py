"""Authentication Rail API client."""

from typing import Any, Optional


class AuthRail:
    """
    Authentication Rail API client.

    Provides authentication and session management:
    - User login with JWT tokens
    - Token refresh and validation
    - User registration
    - Session management and logout
    - CSRF token generation
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Auth rail client."""
        self.http = http_client
        self.base_path = "/api/v1/auth"

    def login(self, email: str, password: str, mfa_code: Optional[str] = None) -> dict:
        """
        Login with email and password.

        Args:
            email: User email
            password: User password
            mfa_code: Optional MFA code

        Returns:
            Login response with tokens or MFA challenge
        """
        data = {"email": email, "password": password, "mfaCode": mfa_code}
        return self.http.post(f"{self.base_path}/login", json=data)

    def refresh_token(self, refresh_token: str) -> dict:
        """
        Refresh access token using refresh token.

        Args:
            refresh_token: Refresh token

        Returns:
            New access token
        """
        return self.http.post(
            f"{self.base_path}/refresh", json={"refreshToken": refresh_token}
        )

    def logout(self, refresh_token: Optional[str] = None) -> dict:
        """
        Logout and invalidate refresh token.

        Args:
            refresh_token: Optional refresh token to invalidate

        Returns:
            Logout confirmation
        """
        data = {}
        if refresh_token:
            data["refreshToken"] = refresh_token
        return self.http.post(f"{self.base_path}/logout", json=data)

    def register(self, data: dict) -> dict:
        """
        Register a new user.

        Args:
            data: Registration data (email, password, name, tenantId)

        Returns:
            Registration confirmation with user details
        """
        return self.http.post(f"{self.base_path}/register", json=data)

    def get_current_user(self) -> dict:
        """
        Get current authenticated user info.

        Returns:
            Current user details
        """
        return self.http.get(f"{self.base_path}/me")

    def get_csrf_token(self) -> dict:
        """
        Get a new CSRF token.

        Returns:
            CSRF token and expiration
        """
        return self.http.get(f"{self.base_path}/csrf")

    def verify_token(self, token: str) -> dict:
        """
        Verify if a token is valid.

        Args:
            token: Token to verify

        Returns:
            Token validity and payload
        """
        return self.http.post(f"{self.base_path}/verify", json={"token": token})
