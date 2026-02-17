"""Klogs Payment Gateway Python Client - Models"""

from typing import Optional, Dict, List
from dataclasses import dataclass, field, asdict
from enum import Enum


class ChargeType(str, Enum):
    """Charge type enumeration"""
    DIRECT_SALE = "directSale"
    PROVISION = "provision"


@dataclass
class CreditCard:
    """Credit card information"""
    card_holder_name: Optional[str] = None
    card_number: Optional[str] = None
    cvv: Optional[str] = None
    expire_month: int = 0
    expire_year: int = 0

    def to_dict(self):
        return {
            "cardHolderName": self.card_holder_name,
            "cardNumber": self.card_number,
            "cvv": self.cvv,
            "expireMonth": self.expire_month,
            "expireYear": self.expire_year
        }


@dataclass
class Reward:
    """Reward information"""
    amount: float = 0.0
    use_reward: bool = False

    def to_dict(self):
        return {
            "amount": self.amount,
            "useReward": self.use_reward
        }


@dataclass
class Address:
    """Address information"""
    name: Optional[str] = None
    surname: Optional[str] = None
    country_code: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    number: Optional[str] = None
    postal_code: Optional[str] = None
    company: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "countryCode": self.country_code,
            "city": self.city,
            "district": self.district,
            "street1": self.street1,
            "street2": self.street2,
            "number": self.number,
            "postalCode": self.postal_code,
            "company": self.company,
            "phone": self.phone,
            "fax": self.fax
        }


@dataclass
class Product:
    """Product information"""
    id: Optional[str] = None
    category: Optional[str] = None
    quantity: float = 0.0
    code: Optional[str] = None
    description: Optional[str] = None
    price: float = 0.0

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "quantity": self.quantity,
            "code": self.code,
            "description": self.description,
            "price": self.price
        }


@dataclass
class CreatePaymentRequest:
    """Payment request model"""
    amount: float
    installment: int
    token: Optional[str] = None
    reference_code: Optional[str] = None
    use_stored_card: bool = False
    card: Optional[CreditCard] = None
    reward: Optional[Reward] = None
    invoice: Optional[Address] = None
    shipping: Optional[Address] = None
    explanation: Optional[str] = None
    use_3d: bool = False
    additional_data: Optional[Dict[str, str]] = None
    currency: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    return_url: Optional[str] = None
    charge_type: Optional[ChargeType] = None
    payment_system_id: Optional[str] = None
    national_number: Optional[str] = None
    products: Optional[List[Product]] = None

    def to_dict(self):
        data = {
            "token": self.token,
            "amount": self.amount,
            "installment": self.installment,
            "referenceCode": self.reference_code,
            "useStoredCard": self.use_stored_card,
            "card": self.card.to_dict() if self.card else None,
            "reward": self.reward.to_dict() if self.reward else None,
            "invoice": self.invoice.to_dict() if self.invoice else None,
            "shipping": self.shipping.to_dict() if self.shipping else None,
            "explanation": self.explanation,
            "use3d": self.use_3d,
            "additionalData": self.additional_data,
            "currency": self.currency,
            "email": self.email,
            "phone": self.phone,
            "returnURL": self.return_url,
            "chargeType": self.charge_type.value if self.charge_type else None,
            "paymentSystemId": self.payment_system_id,
            "nationalNumber": self.national_number,
            "products": [p.to_dict() for p in self.products] if self.products else None
        }
        # Remove None values
        return {k: v for k, v in data.items() if v is not None}


@dataclass
class Error:
    """Error information"""
    summary: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(summary=data.get("summary"))


@dataclass
class Response:
    """Base response model"""
    success: bool = False
    error: Optional[Error] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            success=data.get("success", False),
            error=Error.from_dict(data.get("error", {})) if data.get("error") else None
        )


@dataclass
class CardPaymentResponse(Response):
    """Card payment response"""
    behavior: Optional[str] = None
    link: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        base = Response.from_dict(data)
        return cls(
            success=base.success,
            error=base.error,
            behavior=data.get("behavior"),
            link=data.get("link")
        )


@dataclass
class PaymentTokenResponse(Response):
    """Payment token response"""
    token: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        base = Response.from_dict(data)
        return cls(
            success=base.success,
            error=base.error,
            token=data.get("token")
        )


@dataclass
class ProvisionCommitRequest:
    """Provision commit request"""
    reference_code: str
    amount: Optional[float] = None

    def to_dict(self):
        data = {
            "referenceCode": self.reference_code,
            "amount": self.amount
        }
        return {k: v for k, v in data.items() if v is not None}


@dataclass
class CommissionsRequest:
    """Commissions request"""
    amount: Optional[float] = None
    bin_number: Optional[str] = None
    currency: Optional[str] = None

    def to_dict(self):
        return {
            "amount": self.amount,
            "binNumber": self.bin_number,
            "currency": self.currency
        }


@dataclass
class CommissionResponse(Response):
    """Commission response"""
    installments: Optional[List[Dict]] = None

    @classmethod
    def from_dict(cls, data: dict):
        base = Response.from_dict(data)
        return cls(
            success=base.success,
            error=base.error,
            installments=data.get("installments")
        )
