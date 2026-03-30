"""Base HTTP client for all IOF API requests."""

from typing import Any, Dict, List, Optional, Union

import httpx

from .exceptions import (
    ConnectionError,
    TimeoutError,
    create_api_error,
)


class BaseClient:
    """Base HTTP client with convenience methods for all API requests.

    Provides get/post/patch/delete methods used by all rail clients.
    Uses httpx for HTTP transport and integrates with IOF exception hierarchy.
    """

    def __init__(self, api_key: str, base_url: str, timeout: int = 30) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._client = httpx.Client(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": "IOF-Python-SDK/1.0.0",
            },
            timeout=timeout,
        )

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        stream: bool = False,
    ) -> Any:
        """Make an HTTP request to the IOF API.

        Args:
            method: HTTP method (GET, POST, PATCH, DELETE)
            path: API path (e.g. /api/v1/contracts)
            params: Query parameters
            json: JSON request body
            stream: If True, return raw bytes

        Returns:
            Parsed JSON response or raw bytes if stream=True

        Raises:
            ApiError: On 4xx/5xx responses (subclassed by status code)
            TimeoutError: On request timeout
            ConnectionError: On connection failure
        """
        # Remove None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        # Remove None values from json body
        if isinstance(json, dict):
            json = {k: v for k, v in json.items() if v is not None}

        try:
            response = self._client.request(
                method=method,
                url=path,
                params=params,
                json=json,
            )
        except httpx.TimeoutException:
            raise TimeoutError(f"Request to {method} {path} timed out after {self.timeout}s")
        except httpx.ConnectError:
            raise ConnectionError(f"Failed to connect to {self.base_url}")

        if response.status_code >= 400:
            try:
                error_body = response.json()
                message = error_body.get("message", response.text)
                code = error_body.get("code")
                details = error_body.get("details")
            except Exception:
                message = response.text or f"HTTP {response.status_code}"
                code = None
                details = None
            raise create_api_error(response.status_code, message, code, details)

        if stream:
            return response.content

        if not response.text:
            return None

        return response.json()

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, stream: bool = False) -> Any:
        """HTTP GET request."""
        return self.request("GET", path, params=params, stream=stream)

    def post(self, path: str, json: Optional[Any] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """HTTP POST request."""
        return self.request("POST", path, json=json, params=params)

    def patch(self, path: str, json: Optional[Any] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """HTTP PATCH request."""
        return self.request("PATCH", path, json=json, params=params)

    def delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """HTTP DELETE request."""
        return self.request("DELETE", path, params=params)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "BaseClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
