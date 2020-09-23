from typing import List
from dataclasses import dataclass, field

from .base import BaseImopayObj
from ..exceptions import FieldError
from ..validators import validate_obj_attr_type, validate_obj_attr_in_collection


@dataclass
class BaseTransaction(BaseImopayObj):
    payer: str
    receiver: str
    reference_id: str
    amount: int
    description: str


@dataclass
class Configuration(BaseImopayObj):
    value: int
    charge_type: str

    def _validate_value(self):
        if self.value <= 0:
            raise FieldError("value", "O valor é menor do que 1!")

    def _validate_charge_type(self):
        types = []
        validate_obj_attr_in_collection(self, "charge_type", types)


@dataclass
class DiscountConfiguration(Configuration):
    date: str

    def _validate_date(self):
        # TODO validar data!
        pass


@dataclass
class InvoiceConfigurations(BaseImopayObj):
    fine: Configuration
    interest: Configuration
    discounts: List[DiscountConfiguration] = field(default=list)

    def _validate_fine(self):
        validate_obj_attr_type(self, "fine", dict)

    def _validate_interest(self):
        validate_obj_attr_type(self, "interest", dict)

    def _validate_discounts(self):
        validate_obj_attr_type(self, "discounts", list)

        for discount in self.discounts:
            validate_obj_attr_type(self, "discounts", dict, value=discount)

    def _init_nested_fields(self):
        self.fine = Configuration.from_dict(self.fine)
        self.interest = Configuration.from_dict(self.interest)
        if self.discounts:
            for i, discount in enumerate(self.discounts):
                self.discounts[i] = DiscountConfiguration.from_dict(discount)

    def to_dict(self):
        """
        Por causa do typehint 'List' o to_dict original não funciona!

        Ao invés de solucionar isso, mais fácil sobreescrever o método
        no momento.
        """
        data = {}
        if self.fine:
            data["fine"] = self.fine.to_dict()

        if self.interest:
            data["interest"] = self.interest.to_dict()

        if self.discounts:
            data["discounts"] = [discount.to_dict() for discount in self.discounts]
        return data


@dataclass
class Invoice(BaseImopayObj):
    expiration_date: str
    limit_date: str
    configurations: InvoiceConfigurations = field(default_factory=dict)

    def _init_nested_fields(self):
        self.configurations = InvoiceConfigurations.from_dict(self.configurations)

    def _validate_configurations(self):
        validate_obj_attr_type(self, "configurations", dict)


@dataclass
class InvoiceTransaction(BaseTransaction):
    payment_method: Invoice

    def _init_nested_fields(self):
        self.payment_method = Invoice.from_dict(self.payment_method)

    def _validate_payment_method(self):
        validate_obj_attr_type(self, "payment_method", dict)
