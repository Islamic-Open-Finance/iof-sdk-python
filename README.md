# Islamic Open Finance™ Platform - Python SDK

Official Python SDK for the Islamic Open Finance™ Platform. Build Shariah-compliant financial applications with ease.

## Overview

Typed client for **109 Shariah-native rails across 19 categories** (142+ endpoints) composed from **10 native domain engines** over a single double-entry ledger. Two of those engines are the platform's defensible moats you call through this SDK:

- **`client.settlement.*`** — Settlement Engine. 24×7×365 DvP/FOP/RVP/DFP finality for Murabaha, Ijarah, Salam, Sukuk. AAOIFI SS-1/8/10/17/21/30 enforced at the state machine; CSDR Art. 7 penalties priced pre-confirm; ribawi-pair netting honoured. Reclaims 60–140 bps per corridor.
- **`client.evidence.*`** — Evidence Engine. Signed, tamper-evident compliance pack emitted on every trade: 47/54 controls across SOC 2, ISO 27001, AAOIFI, GDPR, PSD2, IFSB and ISO 20022, SHA-256 Merkle root + HMAC signature, one-call verification. Reclaims 30–55 bps on audit + re-papering.

Combined: **100–195 bps** of Islamic-finance friction reclaimed per corridor — no core replacement.

## Installation

```bash
pip install iof-sdk
```

## Quick Start

```python
from iof_sdk import IOFClient

# Initialize client
client = IOFClient(api_key='your-api-key')

# List accounts
accounts = client.accounts.list_accounts(user_id='user123')

# Get account balance
balance = client.accounts.get_account_balance(account_id='acc_123')

# List transactions
transactions = client.accounts.list_transactions(
    account_id='acc_123',
    from_date='2024-01-01',
    to_date='2024-12-31'
)

# Calculate zakat
zakat = client.accounts.calculate_zakat(
    account_id='acc_123',
    nisab=5000.00
)
```

## Features

- **109 Shariah-Native Rails** - Complete API coverage
- **Type Hints** - Full typing support for IDE autocomplete
- **Async Support** - Coming soon
- **Comprehensive Documentation** - Detailed guides and examples
- **Battle-tested** - Production-ready and SOC2 compliant

## Documentation

Visit [docs.islamicopenfinance.com](https://docs.islamicopenfinance.com) for complete documentation.

## Support

- Email: support@islamicopenfinance.com
- GitHub Issues: [github.com/islamic-open-finance/sdk-python/issues](https://github.com/islamic-open-finance/sdk-python/issues)
- Slack Community: [slack.islamicopenfinance.com](https://slack.islamicopenfinance.com)

## License

Apache-2.0. Copyright 2025 Islamic Open Finance™. All rights reserved.
