"""Klogs Payment Gateway - Payment Transaction Service"""

from typing import TYPE_CHECKING, Optional, Dict, Any

from ..models import RefundRequest, VoidRequest, Response

if TYPE_CHECKING:
    from ..client import KlogsHttpClient


class PaymentTransactionService:
    """Payment Transaction service client"""

    def __init__(self, http_client: 'KlogsHttpClient'):
        self.http = http_client

    def detail(self, referenceCode: str) -> Any:
        """Retrieves transaction details by reference code."""
        return self.http.get(f"/api/trx/{referenceCode}")

    def refund(self, request: RefundRequest) -> Response:
        """Refunds a transaction."""
        return self.http.post("/api/trx/refund", body=request, response_class=Response)

    def void(self, request: VoidRequest) -> Response:
        """Voids (cancels) a transaction."""
        return self.http.post("/api/trx/void", body=request, response_class=Response)
