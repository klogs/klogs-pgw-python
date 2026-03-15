"""Klogs Payment Gateway Python Client"""

from typing import Optional, Dict

from .client import KlogsHttpClient
from .services.card_payment import CardPaymentService
from .services.hosted_payment import HostedPaymentService
from .services.payment_channel import PaymentChannelService
from .services.payment_link import PaymentLinkService
from .services.payment_system_group import PaymentSystemGroupService
from .services.payment_system import PaymentSystemService
from .services.payment_transaction import PaymentTransactionService


__version__ = "1.0.0"


class KlogsClient:
    """Main Klogs Payment Gateway client"""
    
    def __init__(self, api_key: str, secret_key: str, 
                 base_url: str = "https://pgw.klogs.io",
                 additional_headers: Optional[Dict[str, str]] = None):
        """
        Initialize Klogs Payment Gateway client.
        
        Args:
            api_key: API key for authentication
            secret_key: Secret key for authentication
            base_url: Base URL for the API (default: https://pgw.klogs.io)
            additional_headers: Additional headers to include in all requests
        
        Example:
            >>> client = KlogsClient(
            ...     api_key="your-api-key",
            ...     secret_key="your-secret-key"
            ... )
            >>> response = client.card_payment.pay(payment_request)
        """
        self._http_client = KlogsHttpClient(
            base_url=base_url,
            api_key=api_key,
            secret_key=secret_key,
            additional_headers=additional_headers
        )
        
        self._card_payment = CardPaymentService(self._http_client)
        self._hosted_payment = HostedPaymentService(self._http_client)
        self._payment_channel = PaymentChannelService(self._http_client)
        self._payment_link = PaymentLinkService(self._http_client)
        self._payment_system_group = PaymentSystemGroupService(self._http_client)
        self._payment_system = PaymentSystemService(self._http_client)
        self._transaction = PaymentTransactionService(self._http_client)
    
    @property
    def card_payment(self) -> CardPaymentService:
        return self._card_payment

    @property
    def hosted_payment(self) -> HostedPaymentService:
        return self._hosted_payment

    @property
    def payment_channel(self) -> PaymentChannelService:
        return self._payment_channel

    @property
    def payment_link(self) -> PaymentLinkService:
        return self._payment_link

    @property
    def payment_system_group(self) -> PaymentSystemGroupService:
        return self._payment_system_group

    @property
    def payment_system(self) -> PaymentSystemService:
        return self._payment_system

    @property
    def transaction(self) -> PaymentTransactionService:
        return self._transaction


# Export main classes and models
from .models import (
    CreatePaymentRequest,
    CreditCard,
    Reward,
    Address,
    Product,
    ChargeType,
    CardPaymentResponse,
    PaymentTokenResponse,
    ProvisionCommitRequest,
    CommissionsRequest,
    CommissionResponse,
    HostedPaymentRequest,
    CreateHostedPaymentResponse,
    RefundRequest,
    VoidRequest,
    Response,
    Error
)

__all__ = [
    'KlogsClient',
    'CreatePaymentRequest',
    'CreditCard',
    'Reward',
    'Address',
    'Product',
    'ChargeType',
    'CardPaymentResponse',
    'PaymentTokenResponse',
    'ProvisionCommitRequest',
    'CommissionsRequest',
    'CommissionResponse',
    'HostedPaymentRequest',
    'CreateHostedPaymentResponse',
    'RefundRequest',
    'VoidRequest',
    'Response',
    'Error',
    '__version__'
]
