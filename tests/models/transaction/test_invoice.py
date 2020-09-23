from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.models.transaction import Invoice, BaseConfiguration
from imopay_wrapper.exceptions import FieldError


class InvoiceTestCase(TestCase):
    def test_validate_configurations_1(self):
        """
        Dado:
            - uma instância qualquer com configurations={}
        Quando:
            - for chamado Invoice._validate_configurations(instance)
        Então:
            - N/A
        """
        instance = MagicMock(configurations={})

        Invoice._validate_configurations(instance)

    def test_validate_configurations_2(self):
        """
        Dado:
            - uma lista de valores inválidos de configurations
        Quando:
            - for chamado InvoiceTransaction._validate_configurations(instance)
                com o payment_method para cada valor inválido
        Então:
            - deve ser levantado um FieldError para cada valor
        """
        invalid_values = ["1", 3, [], None, Invoice]
        instance = MagicMock()

        for value in invalid_values:
            with self.subTest(value), self.assertRaises(FieldError):
                instance.configurations = value
                Invoice._validate_configurations(instance)

    def test_validate_expiration_date_1(self):
        """
        Dado:
            - uma lista de valores válidos
            - uma instância qualquer
        Quando:
            - for chamado Invoice._validate_expiration_date(instance) para cada valor
                com o valor estando na instância
        Então:
            - N/A
        """
        valid_values = ["2020-08-28", "0000-18-00", "2020-12-20"]

        instance = MagicMock()

        for value in valid_values:
            with self.subTest(value):
                instance.expiration_date = value
                # noinspection PyCallByClass
                Invoice._validate_expiration_date(instance)

    def test_validate_expiration_date_2(self):
        """
        Dado:
            - um mapeamento invalid_values_by_error de vários erros
                para listas de valores inválidos
                {
                    FieldError: ['-1', 0],
                    TypeError: [[], None, {}],
                    ValueError: ['a']
                }
            - uma instância qualquer
        Quando:
            - for chamado Invoice._validate_expiration_date(instance) para
                cada erro e valor com o valor estando na instância
        Então:
            - deve ser lançado o erro específico para cada valor
        """
        invalid_values_by_error = {
            FieldError: ["-1", "a"],
            TypeError: [0, {}, [], None],
        }

        instance = MagicMock()

        for error, values in invalid_values_by_error.items():
            with self.subTest(values):
                for value in values:
                    with self.subTest(value), self.assertRaises(error):
                        instance.expiration_date = value

                        # noinspection PyCallByClass
                        Invoice._validate_expiration_date(instance)

    def test_validate_limit_date_1(self):
        """
        Dado:
            - uma lista de valores válidos
            - uma instância qualquer
        Quando:
            - for chamado Invoice._validate_limit_date(instance) para cada valor
                com o valor estando na instância
        Então:
            - N/A
        """
        valid_values = ["2020-08-28", "0000-18-00", "2020-12-20"]

        instance = MagicMock()

        for value in valid_values:
            with self.subTest(value):
                instance.limit_date = value
                # noinspection PyCallByClass
                Invoice._validate_limit_date(instance)

    def test_validate_limit_date_2(self):
        """
        Dado:
            - um mapeamento invalid_values_by_error de vários erros para
                listas de valores inválidos
                {
                    FieldError: ['-1', 0],
                    TypeError: [[], None, {}],
                    ValueError: ['a']
                }
            - uma instância qualquer
        Quando:
            - for chamado Invoice._validate_limit_date(instance) para cada erro e valor
                com o valor estando na instância
        Então:
            - deve ser lançado o erro específico para cada valor
        """
        invalid_values_by_error = {
            FieldError: ["-1", "a"],
            TypeError: [0, {}, [], None],
        }

        instance = MagicMock()

        for error, values in invalid_values_by_error.items():
            with self.subTest(values):
                for value in values:
                    with self.subTest(value), self.assertRaises(error):
                        instance.limit_date = value

                        # noinspection PyCallByClass
                        Invoice._validate_limit_date(instance)

    def test_init_nested_fields_1(self):
        instance = MagicMock(
            configurations={
                "fine": {
                    "value": 1,
                    "charge_type": BaseConfiguration.FIXED,
                },
                "interest": {
                    "value": 1,
                    "charge_type": BaseConfiguration.DAILY_FIXED,
                },
                "discounts": [
                    {
                        "value": 1,
                        "charge_type": BaseConfiguration.FIXED,
                        "date": "2020-08-28",
                    }
                ],
            }
        )

        Invoice._init_nested_fields(instance)

        self.assertEqual(instance.configurations.fine.value, 1)
        self.assertEqual(instance.configurations.interest.value, 1)
        self.assertEqual(instance.configurations.discounts[0].value, 1)
