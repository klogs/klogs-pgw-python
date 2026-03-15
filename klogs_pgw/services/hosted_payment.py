"""Klogs Payment Gateway - Hosted Payment Service"""

from typing import TYPE_CHECKING

from ..models import HostedPaymentRequest, CreateHostedPaymentResponse

if TYPE_CHECKING:
    from ..client import KlogsHttpClient


class HostedPaymentService:
    """Hosted Payment (payment page) service client"""

    def __init__(self, http_client: 'KlogsHttpClient'):
        self.http = http_client

    def create_payment(self, request: HostedPaymentRequest) -> CreateHostedPaymentResponse:
        """Creates a hosted payment and returns a payment page link."""
        return self.http.post(
            "/api/payment",
            body=request,
            response_class=CreateHostedPaymentResponse
        )
