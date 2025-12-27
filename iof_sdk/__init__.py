"""
Islamic Open Finance Python SDK.

A comprehensive Python client for the Islamic Open Finance platform API.
"""

__version__ = "0.1.0"

from .client import IOFClient, HttpClient
from .exceptions import (
    ApiError,
    AuthenticationError,
    AuthorizationError,
    ConnectionError,
    IOFError,
    NotFoundError,
    RateLimitError,
    ServerError,
    TimeoutError,
    ValidationError,
)

__all__ = [
    "IOFClient",
    "HttpClient",
    "IOFError",
    "ApiError",
    "AuthenticationError",
    "AuthorizationError",
    "NotFoundError",
    "ValidationError",
    "RateLimitError",
    "ServerError",
    "TimeoutError",
    "ConnectionError",
    "__version__",
]
