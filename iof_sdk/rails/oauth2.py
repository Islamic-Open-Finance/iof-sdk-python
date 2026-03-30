"""OAuth 2.0 / OpenID Connect Rail API client."""

from typing import Any, Optional
from urllib.parse import urlencode


class OAuth2Rail:
    """
    OAuth 2.0 / OpenID Connect Rail API client.

    Provides OAuth 2.0 authorization capabilities:
    - Authorization Code Flow
    - Client Credentials Flow
    - Token Refresh and Revocation
    - Dynamic Client Registration
    - OpenID Connect UserInfo
    - Server Metadata
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the OAuth 2.0 rail client."""
        self.http = http_client
        self.base_path = "/api/v1/oauth2"

    def build_authorize_url(
        self,
        base_url: str,
        response_type: str,
        client_id: str,
        redirect_uri: str,
        scope: Optional[str] = None,
        state: Optional[str] = None,
        nonce: Optional[str] = None,
        code_challenge: Optional[str] = None,
        code_challenge_method: Optional[str] = None,
    ) -> str:
        """
        Build an authorization URL.

        Args:
            base_url: API base URL
            response_type: Response type (code, token, id_token)
            client_id: Client ID
            redirect_uri: Redirect URI
            scope: Optional scope
            state: Optional state
            nonce: Optional nonce
            code_challenge: Optional PKCE code challenge
            code_challenge_method: Optional code challenge method (S256, plain)

        Returns:
            Authorization URL string
        """
        params = {
            "response_type": response_type,
            "client_id": client_id,
            "redirect_uri": redirect_uri,
        }
        if scope:
            params["scope"] = scope
        if state:
            params["state"] = state
        if nonce:
            params["nonce"] = nonce
        if code_challenge:
            params["code_challenge"] = code_challenge
        if code_challenge_method:
            params["code_challenge_method"] = code_challenge_method

        return f"{base_url}{self.base_path}/authorize?{urlencode(params)}"

    # Token Exchange

    def exchange_token(self, data: dict) -> dict:
        """
        Exchange tokens (generic token endpoint).

        Args:
            data: Token request data (grant_type, code, client_id, etc.)

        Returns:
            Token response (access_token, token_type, expires_in, etc.)
        """
        return self.http.post(f"{self.base_path}/token", json=data)

    def exchange_authorization_code(
        self,
        code: str,
        client_id: str,
        redirect_uri: str,
        client_secret: Optional[str] = None,
        code_verifier: Optional[str] = None,
    ) -> dict:
        """
        Exchange an authorization code for tokens.

        Args:
            code: Authorization code
            client_id: Client ID
            redirect_uri: Redirect URI
            client_secret: Optional client secret
            code_verifier: Optional PKCE code verifier

        Returns:
            Token response
        """
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "client_secret": client_secret,
            "code_verifier": code_verifier,
        }
        return self.http.post(f"{self.base_path}/token", json=data)

    def refresh_token(
        self,
        refresh_token: str,
        client_id: str,
        client_secret: Optional[str] = None,
    ) -> dict:
        """
        Refresh an access token.

        Args:
            refresh_token: Refresh token
            client_id: Client ID
            client_secret: Optional client secret

        Returns:
            Token response
        """
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        return self.http.post(f"{self.base_path}/token", json=data)

    def get_client_credentials_token(
        self,
        client_id: str,
        client_secret: str,
        scope: Optional[str] = None,
    ) -> dict:
        """
        Get a token using client credentials.

        Args:
            client_id: Client ID
            client_secret: Client secret
            scope: Optional scope

        Returns:
            Token response
        """
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": scope,
        }
        return self.http.post(f"{self.base_path}/token", json=data)

    # Token Revocation

    def revoke_token(
        self, token: str, token_type_hint: Optional[str] = None
    ) -> dict:
        """
        Revoke a token.

        Args:
            token: Token to revoke
            token_type_hint: Optional hint (access_token, refresh_token)

        Returns:
            Success response
        """
        data = {"token": token, "token_type_hint": token_type_hint}
        return self.http.post(f"{self.base_path}/revoke", json=data)

    # Dynamic Client Registration

    def register_client(self, data: dict) -> dict:
        """
        Register a new OAuth 2.0 client.

        Args:
            data: Client registration data (client_name, redirect_uris, etc.)

        Returns:
            Client registration response with client_id and client_secret
        """
        return self.http.post(f"{self.base_path}/register", json=data)

    # Server Metadata

    def get_server_metadata(self) -> dict:
        """
        Get OAuth 2.0 server metadata.

        Returns:
            Server metadata
        """
        return self.http.get(
            "/api/v1/.well-known/oauth-authorization-server"
        )

    def get_openid_configuration(self) -> dict:
        """
        Get OpenID Connect configuration.

        Returns:
            OpenID configuration
        """
        return self.http.get("/api/v1/.well-known/openid-configuration")

    # UserInfo

    def get_user_info(self, access_token: str) -> dict:
        """
        Get user info from the UserInfo endpoint.

        Args:
            access_token: Access token

        Returns:
            User info
        """
        return self.http.get(f"{self.base_path}/userinfo")
