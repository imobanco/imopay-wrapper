from typing import List
from dataclasses import dataclass, field

from .base import BaseImopayObj


# @dataclass
# class BaseTransaction(BaseImopayObj):



@dataclass
class Configuration(BaseImopayObj):
    value: str
    type: str
    charge_type: str
    days: str


@dataclass
class InvoiceConfigurations(BaseImopayObj):
    fine: Configuration
    interest: Configuration
    discounts: List[Configuration] = field(default=list)

    def __post_init__(self):
        if isinstance(self.fine, dict):
            self.fine = Configuration.from_dict(self.fine)
        if isinstance(self.interest, dict):
            self.interest = Configuration.from_dict(self.interest)
        if self.discounts:
            for i, discount in enumerate(self.discounts):
                if isinstance(discount, dict):
                    self.discounts[i] = Configuration.from_dict(discount)


@dataclass
class Invoice(BaseImopayObj):
    expiration_date: str
    limit_date: str
    configurations: InvoiceConfigurations

    def __post_init__(self):
        if isinstance(self.configurations, dict):
            self.configurations = InvoiceConfigurations.from_dict(self.configurations)


@dataclass
class InvoiceTransaction(BaseImopayObj):
    payment_method: Invoice
    payer: str
    receiver: str
    reference_id: str
    amount: int
    description: str

    def __post_init__(self):
        if isinstance(self.payment_method, dict):
            self.payment_method = Invoice.from_dict(self.payment_method)
