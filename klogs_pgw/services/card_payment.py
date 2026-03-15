"""Klogs Payment Gateway - Card Payment Service"""

from typing import TYPE_CHECKING

from ..models import (
    CardPaymentResponse,
    CreatePaymentRequest,
    PaymentTokenResponse,
    ProvisionCommitRequest,
    CommissionsRequest,
    CommissionResponse,
    RefundRequest,
    VoidRequest,
    Response
)

if TYPE_CHECKING:
    from ..client import KlogsHttpClient


class CardPaymentService:
    """Card Payment service client"""
    
    def __init__(self, http_client: 'KlogsHttpClient'):
        self.http = http_client
    
    def pay(self, request: CreatePaymentRequest) -> CardPaymentResponse:
        return self.http.post(
            "/api/cardPayment",
            body=request,
            response_class=CardPaymentResponse
        )
    
    def create_payment_token(self) -> PaymentTokenResponse:
        return self.http.get(
            "/api/cardPayment/token",
            response_class=PaymentTokenResponse
        )
    
    def provision_commit(self, request: ProvisionCommitRequest) -> Response:
        return self.http.post(
            "/api/cardPayment/provisionCommit",
            body=request,
            response_class=Response
        )
    
    def get_commissions_by_bin(self, request: CommissionsRequest) -> CommissionResponse:
        params = []
        if request.amount is not None:
            params.append(('amount', str(request.amount)))
        if request.bin_number:
            params.append(('binNumber', request.bin_number))
        if request.currency:
            params.append(('currency', request.currency))
        if request.cardId:
            params.append(('cardId', request.cardId))
        if request.product_codes:
            for code in request.product_codes:
                params.append(('productCode', code))
        if request.product_category_codes:
            for code in request.product_category_codes:
                params.append(('productCategoryCode', code))
        
        return self.http.get(
            "/api/cardPayment/installments",
            params=params,
            response_class=CommissionResponse
        )
