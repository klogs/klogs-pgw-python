# klogs-pgw-python
Klogs Payment Gateway Python client package

## Installation

```bash
pip install klogs-pgw
```

## Usage

### Basic Payment Request

```python
from klogs_pgw import KlogsClient
from klogs_pgw.models import CreatePaymentRequest, CreditCard

# Initialize client
client = KlogsClient(
    api_key="lrM54xgeBRw6kABrmyz5GixNW54Eg9zWt3Orgi35E",
    secret_key="G99T1V+bzzfU+X0Zv+xvCB4LwLstYtymL8ybsZjvdLGzl98EuNh3AeYUCA1pAOYa6rxv3Y5HsFvhs2v3ufx+nQ==",
    base_url="https://pgw.klogs.io"
)

# Create payment request
payment_request = CreatePaymentRequest(
    amount=15,
    installment=1,
    reference_code="TEST-123123123",
    card=CreditCard(
        card_holder_name="Nadir Yıldız",
        card_number="5526080000000006",
        cvv="423",
        expire_month=4,
        expire_year=2027
    ),
    explanation="Test from python client",
    use_3d=True,
    currency="TRY",
    email="info@klogs.io",
    phone="5554443322"
)

# Make payment
response = client.card_payment.pay(payment_request)

if response.success:
    print(f"Behavior: {response.behavior}")
    print(f"Success: {response.success}")
else:
    print(f"Error: {response.error.summary}")
```

## Features

- Card Payment
- Hosted Payment
- Payment Channels
- Payment Systems
- Payment Transactions
- Automatic request signing with HMAC-SHA256

## License

MIT
