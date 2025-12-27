# Islamic Open Finance Python SDK

Official Python client library for the Islamic Open Finance (IOF) platform API.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

## Installation

```bash
pip install iof-sdk
```

Or install from source:

```bash
cd packages/sdk-python
pip install -e .
```

## Features

- 🏦 **Comprehensive Rail Support** - All 27 Islamic Finance rails included
- 🔄 **Async & Sync** - Both synchronous and asynchronous HTTP clients
- 🔒 **Type Safe** - Full type hints with TypedDict models
- 🔑 **Multi-Auth** - API key and Bearer token authentication
- 🏢 **Multi-Tenant** - Built-in tenant isolation support
- ⚡ **Retry Logic** - Automatic retry with exponential backoff
- 📄 **Pagination** - Helper methods for paginated responses

## Quick Start

```python
from iof_sdk import IOFClient

# Initialize the client
client = IOFClient(
    base_url="https://api.islamicopenfinance.com",
    api_key="your-api-key",
    tenant_id="tenant-123"
)

# Contracts Rail
contracts = client.contracts.list_contracts(status="ACTIVE", page=1, limit=50)
contract = client.contracts.create_contract({
    "contract_type": "MURABAHA",
    "customer_id": "CUST-123",
    "amount": 100000.00,
    "currency": "USD"
})

# AML/CFT Rail
screening = client.aml.create_screening({
    "subject_id": "CUST-456",
    "screening_type": "PEP",
    "country_codes": ["US", "GB"]
})
alerts = client.aml.list_alerts(severity="HIGH", status="OPEN")

# Developer Rail
api_key = client.developer.create_api_key({
    "client_id": "app-789",
    "key_name": "Production Key",
    "environment": "PRODUCTION",
    "scopes": ["contracts:read", "contracts:write"]
})

# Partners Rail
partners = client.partners.list_partners(tier="PLATINUM")
revenue_share = client.partners.create_revenue_share({
    "partner_id": "PTR-123",
    "program_id": "PROG-456",
    "period_start": "2025-01-01",
    "period_end": "2025-01-31"
})

# Zakat Rail
profile = client.zakat.create_profile({
    "subject_type": "INDIVIDUAL",
    "subject_id": "USER-789",
    "methodology": "NET_ASSETS"
})
calculation = client.zakat.create_calculation({
    "profile_id": "ZKT-123",
    "as_of_date": "2025-12-31"
})

# Observability Rail
audit_logs = client.observability.query_audit_logs(
    rail="CONTRACTS",
    from_date="2025-01-01",
    to_date="2025-01-31"
)
```

## Available Rails

### Core Rails

- **Contracts** - Islamic finance contract lifecycle management
- **Jurisdictions** - Multi-jurisdiction regulatory configurations

### Access & Identity Rails

- **Access Consent** - Open Banking consent management (AISP/PISP)
- **KYC** - Customer verification and screening
- **AML** - Anti-Money Laundering and CFT compliance
- **Consent** - GDPR/CCPA privacy and data protection

### Developer & Partner Rails

- **Developer** - API keys, client apps, webhooks
- **Partners** - Partner programs and revenue sharing

### Operations Rails

- **Cases** - Case management
- **Disputes** - Dispute and collections management
- **Zakat** - Zakat calculation and purification
- **Reconciliation** - Transaction reconciliation and matching
- **Routing** - Payment and message routing rules

### Financial Rails

- **Messages** - ISO 20022 messaging
- **Clearing** - Settlement and multilateral netting
- **Treasury** - Liquidity and cash management
- **Risk** - Exposure and limit management
- **Portfolio** - Investment mandate and portfolio management
- **Reporting** - Analytics and report generation
- **Analytics** - Advanced analytics and insights

### Governance Rails

- **Legal** - Legal template and document management
- **Underwriting** - Credit and risk assessment
- **Compliance** - Regulatory and Shariah compliance
- **Governance** - Shariah board and committee management

### Event & Notification Rails

- **Events** - Event publishing and webhook management
- **Notifications** - Multi-channel notifications
- **Search** - Full-text search across entities
- **Webhooks** - Webhook subscription and delivery

### Observability Rails

- **Observability** - SLOs, audit logs, Shariah monitoring

## Authentication

### API Key Authentication

```python
client = IOFClient(
    base_url="https://api.example.com",
    api_key="your-api-key"
)
```

### Bearer Token Authentication

```python
client = IOFClient(
    base_url="https://api.example.com",
    access_token="your-access-token"
)
```

### Multi-Tenant Support

```python
client = IOFClient(
    base_url="https://api.example.com",
    api_key="your-api-key",
    tenant_id="tenant-123"
)
```

## Error Handling

```python
from iof_sdk import IOFClient
from iof_sdk.exceptions import (
    AuthenticationError,
    AuthorizationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    ServerError
)

try:
    contract = client.contracts.get_contract("contract-id")
except NotFoundError:
    print("Contract not found")
except AuthorizationError:
    print("Insufficient permissions")
except ValidationError as e:
    print(f"Validation error: {e.message}")
except RateLimitError:
    print("Rate limit exceeded")
except ServerError as e:
    print(f"Server error: {e.status_code}")
```

## Configuration Options

```python
client = IOFClient(
    base_url="https://api.example.com",
    api_key="your-api-key",
    tenant_id="tenant-123",
    timeout=30,  # Request timeout in seconds
    max_retries=3,  # Number of retry attempts
    retry_delay=1.0  # Initial retry delay in seconds
)
```

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black iof_sdk/

# Type checking
mypy iof_sdk/
```

## License

Copyright © 2025 Islamic Open Finance. All rights reserved.

## Support

- Documentation: https://docs.islamicopenfinance.com
- API Reference: https://api.islamicopenfinance.com/docs
- GitHub: https://github.com/Islamic-Open-Finance/app
