# Klogs Payment Gateway Python Client

Official Python client library for Klogs Payment Gateway API. This package provides a simple and intuitive interface for integrating payment processing functionality into your Python applications.

## Features

- **Card Payment Operations**: Direct card payments with 3D Secure support
- **Hosted Payment Pages**: Create secure payment pages for your customers
- **Transaction Management**: Query, refund, and void transactions
- **Installment Queries**: Get commission rates and installment options
- **Provision Operations**: Provision and commit payment flows
- **Automatic Authentication**: HMAC-SHA256 request signing handled automatically
- **Type Safety**: Full dataclass-based models with type hints
- **Easy Integration**: Simple, intuitive API design

## Installation

```bash
pip install klogs-pgw
```

## Quick Start

```python
from klogs_pgw import KlogsClient
from klogs_pgw.models import CreatePaymentRequest, CreditCard

# Initialize client
client = KlogsClient(
    api_key="your-api-key",
    secret_key="your-secret-key",
    base_url="https://pgw.klogs.io"
)

# Create payment request
payment_request = CreatePaymentRequest(
    amount=100.0,
    installment=1,
    reference_code="ORDER-12345",
    card=CreditCard(
        card_holder_name="John Doe",
        card_number="5526080000000006",
        cvv="123",
        expire_month=12,
        expire_year=2025
    ),
    use_3d=True,
    currency="TRY",
    email="customer@example.com",
    phone="5551234567"
)

# Make payment
response = client.card_payment.pay(payment_request)

if response.success:
    print(f"Payment successful! Behavior: {response.behavior}")
    if response.link:
        print(f"3D Secure Link: {response.link}")
else:
    print(f"Payment failed: {response.error.summary}")
```

## Usage Examples

### Card Payment Service

#### Create Payment Token

```python
response = client.card_payment.create_payment_token()
if response.success:
    print(f"Token: {response.token}")
```

#### Get Installment Commissions

```python
from klogs_pgw.models import CommissionsRequest

request = CommissionsRequest(
    amount=500.0,
    bin_number="552608",
    currency="TRY",
    product_codes=["PROD-001", "PROD-002"],
    product_category_codes=["CAT-A", "CAT-B"]
)

response = client.card_payment.get_commissions_by_bin(request)
if response.success:
    for installment in response.installments:
        print(f"Installment: {installment}")
```

#### Provision Commit

```python
from klogs_pgw.models import ProvisionCommitRequest

request = ProvisionCommitRequest(
    reference_code="ORDER-12345",
    amount=100.0
)

response = client.card_payment.provision_commit(request)
if response.success:
    print("Provision committed successfully")
```

### Hosted Payment Service

```python
from klogs_pgw.models import HostedPaymentRequest, ChargeType

request = HostedPaymentRequest(
    amount=250.0,
    currency="TRY",
    reference_code="ORDER-67890",
    full_name="Jane Smith",
    email="jane@example.com",
    phone="5559876543",
    return_url="https://yoursite.com/payment/callback",
    charge_type=ChargeType.DIRECT_SALE,
    explanation="Product purchase"
)

response = client.hosted_payment.create_payment(request)
if response.success:
    print(f"Payment Page: {response.link}")
    print(f"Payment ID: {response.payment_id}")
```

### Transaction Service

#### Get Transaction Details

```python
transaction = client.payment_transaction.detail("ORDER-12345")
print(transaction)
```

#### Refund Transaction

```python
from klogs_pgw.models import RefundRequest

request = RefundRequest(
    reference_code="ORDER-12345",
    amount=50.0
)

response = client.payment_transaction.refund(request)
if response.success:
    print("Refund successful")
```

#### Void Transaction

```python
from klogs_pgw.models import VoidRequest

request = VoidRequest(reference_code="ORDER-12345")

response = client.payment_transaction.void(request)
if response.success:
    print("Transaction voided")
```

## Advanced Usage

### Custom Headers

```python
client = KlogsClient(
    api_key="your-api-key",
    secret_key="your-secret-key",
    base_url="https://pgw.klogs.io",
    additional_headers={"X-Custom-Header": "value"}
)
```

### Payment with Extended Details

```python
from klogs_pgw.models import CreatePaymentRequest, CreditCard, Address, Product

payment_request = CreatePaymentRequest(
    amount=500.0,
    installment=3,
    reference_code="ORDER-12345",
    card=CreditCard(
        card_holder_name="John Doe",
        card_number="5526080000000006",
        cvv="123",
        expire_month=12,
        expire_year=2025
    ),
    invoice=Address(
        name="John",
        surname="Doe",
        country_code="TR",
        city="Istanbul",
        street1="Main Street",
        postal_code="34000",
        phone="5551234567"
    ),
    shipping=Address(
        name="John",
        surname="Doe",
        country_code="TR",
        city="Istanbul",
        street1="Main Street",
        postal_code="34000"
    ),
    products=[
        Product(
            id="PROD-001",
            category="Electronics",
            quantity=1,
            code="SKU-123",
            description="Laptop",
            price=500.0
        )
    ],
    use_3d=True,
    currency="TRY",
    email="john@example.com",
    phone="5551234567",
    save_card=True,
    customer_ip="127.0.0.1"
)

response = client.card_payment.pay(payment_request)
```

## API Reference

### Client Services

- `client.card_payment` - Card payment operations
  - `pay(request)` - Create a card payment
  - `create_payment_token()` - Generate a payment token
  - `get_commissions_by_bin(request)` - Get installment commissions
  - `provision_commit(request)` - Commit a provision

- `client.hosted_payment` - Hosted payment page operations
  - `create_payment(request)` - Create a hosted payment page

- `client.payment_transaction` - Transaction management
  - `detail(reference_code)` - Get transaction details
  - `refund(request)` - Refund a transaction
  - `void(request)` - Void/cancel a transaction

### Models

All request and response models are available in `klogs_pgw.models`:

- `CreatePaymentRequest` - Card payment request
- `HostedPaymentRequest` - Hosted payment request
- `CommissionsRequest` - Installment commission query
- `ProvisionCommitRequest` - Provision commit request
- `RefundRequest` - Refund request
- `VoidRequest` - Void request
- `CreditCard` - Credit card information
- `Address` - Address information
- `Product` - Product information
- `ChargeType` - Charge type enum (`DIRECT_SALE`, `PROVISION`)

## Error Handling

```python
try:
    response = client.card_payment.pay(payment_request)
    if response.success:
        print("Payment successful")
    else:
        print(f"Payment failed: {response.error.summary}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Requirements

- Python 3.7+
- requests

## License

MIT

## Support

For questions and support, please contact Klogs support team or visit the documentation.
