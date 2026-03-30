"""
Islamic Open Finance SDK for Python
====================================

A comprehensive Python SDK for the Islamic Open Finance Platform.
Covers all 142 IOF API rails including Islamic contract types,
Sukuk, Takaful, Waqf, Trade Finance, Basel III, and more.

Usage:
    from iof_sdk import IOFClient

    client = IOFClient(api_key='your-api-key')
    accounts = client.accounts.list_accounts()
    contracts = client.murabaha.list_contracts()
    sukuk = client.sukuk.list_issuances()
"""

__version__ = "1.0.0"

from .base_client import BaseClient
from .client import IOFClient
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
    "BaseClient",
    # Exceptions
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
]
