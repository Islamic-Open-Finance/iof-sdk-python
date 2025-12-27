"""
Custom exceptions for the IOF SDK.

This module provides exception classes for handling various error conditions
that may occur when interacting with the Islamic Open Finance API.
"""

from typing import Any, Dict, Optional


class IOFError(Exception):
    """Base exception for all IOF SDK errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize IOF error.

        Args:
            message: Error message
            details: Additional error details
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}


class ApiError(IOFError):
    """Exception raised when the API returns an error response."""

    def __init__(
        self,
        message: str,
        status_code: int,
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize API error.

        Args:
            message: Error message
            status_code: HTTP status code
            code: API error code
            details: Additional error details
        """
        super().__init__(message, details)
        self.status_code = status_code
        self.code = code or "UNKNOWN_ERROR"


class AuthenticationError(ApiError):
    """Exception raised when authentication fails (401)."""

    def __init__(
        self,
        message: str = "Authentication failed",
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize authentication error."""
        super().__init__(message, 401, code, details)


class AuthorizationError(ApiError):
    """Exception raised when authorization fails (403)."""

    def __init__(
        self,
        message: str = "Authorization failed",
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize authorization error."""
        super().__init__(message, 403, code, details)


class NotFoundError(ApiError):
    """Exception raised when a resource is not found (404)."""

    def __init__(
        self,
        message: str = "Resource not found",
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize not found error."""
        super().__init__(message, 404, code, details)


class ValidationError(ApiError):
    """Exception raised when request validation fails (400, 422)."""

    def __init__(
        self,
        message: str = "Validation failed",
        status_code: int = 400,
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize validation error."""
        super().__init__(message, status_code, code, details)


class RateLimitError(ApiError):
    """Exception raised when rate limit is exceeded (429)."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
        retry_after: Optional[int] = None,
    ) -> None:
        """
        Initialize rate limit error.

        Args:
            message: Error message
            code: API error code
            details: Additional error details
            retry_after: Seconds to wait before retrying
        """
        super().__init__(message, 429, code, details)
        self.retry_after = retry_after


class ServerError(ApiError):
    """Exception raised when the server returns a 5xx error."""

    def __init__(
        self,
        message: str = "Server error",
        status_code: int = 500,
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize server error."""
        super().__init__(message, status_code, code, details)


class TimeoutError(IOFError):
    """Exception raised when a request times out."""

    def __init__(self, message: str = "Request timeout") -> None:
        """Initialize timeout error."""
        super().__init__(message)


class ConnectionError(IOFError):
    """Exception raised when connection to the API fails."""

    def __init__(self, message: str = "Connection failed") -> None:
        """Initialize connection error."""
        super().__init__(message)


def create_api_error(
    status_code: int,
    message: str,
    code: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
) -> ApiError:
    """
    Create the appropriate API error based on status code.

    Args:
        status_code: HTTP status code
        message: Error message
        code: API error code
        details: Additional error details

    Returns:
        Appropriate ApiError subclass instance
    """
    if status_code == 401:
        return AuthenticationError(message, code, details)
    elif status_code == 403:
        return AuthorizationError(message, code, details)
    elif status_code == 404:
        return NotFoundError(message, code, details)
    elif status_code in (400, 422):
        return ValidationError(message, status_code, code, details)
    elif status_code == 429:
        return RateLimitError(message, code, details)
    elif 500 <= status_code < 600:
        return ServerError(message, status_code, code, details)
    else:
        return ApiError(message, status_code, code, details)
