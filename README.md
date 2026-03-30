# Islamic Open Finance™ Platform - Python SDK

Official Python SDK for the Islamic Open Finance™ Platform. Build Shariah-compliant financial applications with ease.

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

- **105 Islamic Finance Rails** - Complete API coverage
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
