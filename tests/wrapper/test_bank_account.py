from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.wrapper.base import (
    CreateMixin,
    RetrieveMixin,
    DestroyMixin,
    GetByDocumentMixin,
)
from imopay_wrapper.models.bank_account import BankAccount


class BankAccountWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().bank_account

    def test_mixins(self):
        """
        Dado:
            - um client ImopayWrapper().bank_account
        Quando:
            - N/A
        Então:
            - client deve ser uma instância de
                CreateMixin, RetrieveMixin, DestroyMixin, GetByDocumentMixin
        """
        mixins = (CreateMixin, RetrieveMixin, DestroyMixin, GetByDocumentMixin)
        for mixin in mixins:
            self.assertIsInstance(
                self.client, mixin
            )

    def test_model(self):
        """
        Dado:
            - um client ImopayWrapper().bank_account
        Quando:
            - N/A
        Então:
            - client.model deve ser BankAccount
        """
        self.assertEqual(self.client.model, BankAccount)

    def test_action(self):
        """
        Dado:
            - um client ImopayWrapper().bank_account
        Quando:
            - N/A
        Então:
            - client.action deve ser 'bank_accounts'
        """
        self.assertEqual(self.client.action, "bank_accounts")
