"""Klogs Payment Gateway - Card Payment Service"""

from typing import TYPE_CHECKING

from ..models import (
    CardPaymentResponse,
    CreatePaymentRequest,
    PaymentTokenResponse,
    ProvisionCommitRequest,
    CommissionsRequest,
    CommissionResponse,
    Response
)

if TYPE_CHECKING:
    from ..client import KlogsHttpClient


class CardPaymentService:
    """Card Payment service client"""
    
    def __init__(self, http_client: 'KlogsHttpClient'):
        """
        Initialize card payment service.
        
        Args:
            http_client: HTTP client instance
        """
        self.http = http_client
    
    def pay(self, request: CreatePaymentRequest) -> CardPaymentResponse:
        """
        Process a card payment.
        
        Args:
            request: Payment request data
            
        Returns:
            Card payment response
        """
        return self.http.post(
            "/api/cardPayment",
            body=request,
            response_class=CardPaymentResponse
        )
    
    def create_payment_token(self) -> PaymentTokenResponse:
        """
        Create a payment token.
        
        Returns:
            Payment token response
        """
        return self.http.get(
            "/api/cardPayment/token",
            response_class=PaymentTokenResponse
        )
    
    def provision_commit(self, request: ProvisionCommitRequest) -> Response:
        """
        Commit a provision.
        
        Args:
            request: Provision commit request
            
        Returns:
            Response
        """
        return self.http.post(
            "/api/cardPayment/provisionCommit",
            body=request,
            response_class=Response
        )
    
    def get_commissions_by_bin(self, request: CommissionsRequest) -> CommissionResponse:
        """
        Get commissions by BIN number.
        
        Args:
            request: Commissions request
            
        Returns:
            Commission response
        """
        params = {}
        if request.amount is not None:
            params['amount'] = str(request.amount)
        if request.bin_number:
            params['binNumber'] = request.bin_number
        if request.currency:
            params['currency'] = request.currency
        
        return self.http.get(
            "/api/cardPayment/installments",
            params=params,
            response_class=CommissionResponse
        )
