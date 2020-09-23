from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.models.transaction import InvoiceTransaction, Invoice
from imopay_wrapper.exceptions import FieldError


class InvoiceTransactionTestCase(TestCase):
    def test_validate_payment_method_1(self):
        """
        Dado:
            - uma instância qualquer com payment_method={}
        Quando:
            - for chamado InvoiceTransaction._validate_payment_method(instance)
        Então:
            - N/A
        """
        instance = MagicMock(payment_method={})

        InvoiceTransaction._validate_payment_method(instance)

    def test_validate_payment_method_2(self):
        """
        Dado:
            - uma lista de valores inválidos de payment_method
        Quando:
            - for chamado InvoiceTransaction._validate_payment_method(instance)
                com o payment_method para cada valor inválido
        Então:
            - deve ser levantado um FieldError para cada valor
        """
        invalid_values = ["1", 3, [], None, InvoiceTransaction]
        instance = MagicMock()

        for value in invalid_values:
            with self.subTest(value), self.assertRaises(FieldError):
                instance.payment_method = value
                InvoiceTransaction._validate_payment_method(instance)

    def test_2(self):
        instance: InvoiceTransaction = MagicMock(
            payment_method={"expiration_date": "2020-08-28", "limit_date": "2020-08-28"}
        )

        InvoiceTransaction._init_nested_fields(instance)

        self.assertIsInstance(instance.payment_method, Invoice)
        self.assertEqual(instance.payment_method.expiration_date, "2020-08-28")
        self.assertEqual(instance.payment_method.limit_date, "2020-08-28")
