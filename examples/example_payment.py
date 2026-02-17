"""
Example: Card Payment with Klogs Payment Gateway Python Client
"""

from klogs_pgw import KlogsClient, CreatePaymentRequest, CreditCard


def main():
    # Initialize the client
    client = KlogsClient(
        api_key="lrM54xgeBRw6kABrmyz5GixNW54Eg9zWt3Orgi35E",
        secret_key="G99T1V+bzzfU+X0Zv+xvCB4LwLstYtymL8ybsZjvdLGzl98EuNh3AeYUCA1pAOYa6rxv3Y5HsFvhs2v3ufx+nQ==",
        base_url="https://pgw.klogs.io"
    )
    
    # Create payment request
    payment_request = CreatePaymentRequest(
        amount=15.0,
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
    
    try:
        # Make payment
        response = client.card_payment.pay(payment_request)
        
        if response.success:
            print(f"Payment successful!")
            print(f"Behavior: {response.behavior}")
            print(f"Link: {response.link}")
        else:
            print(f"Payment failed!")
            if response.error:
                print(f"Error: {response.error.summary}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def example_get_payment_token():
    """Example: Get payment token"""
    client = KlogsClient(
        api_key="your-api-key",
        secret_key="your-secret-key"
    )
    
    try:
        response = client.card_payment.create_payment_token()
        if response.success:
            print(f"Token: {response.token}")
        else:
            print(f"Error: {response.error.summary}")
    except Exception as e:
        print(f"Error: {e}")


def example_get_commissions():
    """Example: Get commissions by BIN"""
    from klogs_pgw import CommissionsRequest
    
    client = KlogsClient(
        api_key="your-api-key",
        secret_key="your-secret-key"
    )
    
    try:
        request = CommissionsRequest(
            amount=100.0,
            bin_number="552608",
            currency="TRY"
        )
        
        response = client.card_payment.get_commissions_by_bin(request)
        if response.success:
            print(f"Installments: {response.installments}")
        else:
            print(f"Error: {response.error.summary}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
