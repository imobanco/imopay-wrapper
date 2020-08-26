from typing import List
from dataclasses import dataclass, field

from .base import BaseImopayObj


@dataclass
class BaseTransaction(BaseImopayObj):
    payer: str
    receiver: str
    reference_id: str
    amount: int
    description: str


@dataclass
class InvoiceConfiguration(BaseImopayObj):
    value: str
    type: str
    charge_type: str
    days: str


@dataclass
class Invoice(BaseImopayObj):
    expiration_date: str
    limit_date: str
    configurations: List[InvoiceConfiguration] = field(default_factory=list)


@dataclass
class InvoiceTransaction(BaseTransaction):
    payment_method: Invoice
