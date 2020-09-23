from unittest import TestCase
from unittest.mock import MagicMock, patch

from imopay_wrapper.models.transaction import (
    BaseConfiguration,
    InterestConfiguration,
    FineConfiguration,
    DiscountConfiguration,
)
from imopay_wrapper.exceptions import FieldError


class BaseConfigurationTestCase(TestCase):
    def test_initial_0(self):
        """
        Dado:
            - um value válido 1
            - um charge_type válido 'p'
                (BaseConfiguration.VALID_CHARGE_TYPES mocado)
            - um data
                {"value": 1, "charge_type": 'p'}
        Quando:
            - for criado um Configuration t a partir do data
        Então:
            - t.value tem que ser igual a value
            - t.charge_type tem que ser igual a charge_type
        """
        value = 1
        charge_type = "p"

        data = {"value": value, "charge_type": charge_type}
        with patch(
            "imopay_wrapper.models.transaction.BaseConfiguration.VALID_CHARGE_TYPES",
            {BaseConfiguration.PERCENTAGE},
        ):
            t = BaseConfiguration.from_dict(data)
        self.assertEqual(t.value, value)
        self.assertEqual(t.charge_type, charge_type)

    def test_validate_value_1(self):
        """
        Dado:
            - uma lista de valores válidos
            - uma instância qualquer
        Quando:
            - for chamado Configuration._validate_value(instance) para cada valor
                com o valor estando na instância
        Então:
            - N/A
        """
        valid_values = ["1", 3, "15", "124123", 19247736471]

        instance = MagicMock()

        for value in valid_values:
            with self.subTest(value):
                instance.value = value

                # noinspection PyCallByClass
                BaseConfiguration._validate_value(instance)

    def test_validate_value_2(self):
        """
        Dado:
            - um mapeamento invalid_values_by_error de vários erros para listas de valores inválidos
                {
                    FieldError: ['-1', 0],
                    TypeError: [[], None, {}],
                    ValueError: ['a']
                }
            - uma instância qualquer
        Quando:
            - for chamado Configuration._validate_value(instance) para cada erro e valor
                com o valor estando na instância
        Então:
            - deve ser lançado o erro específico para cada valor
        """
        invalid_values_by_error = {
            FieldError: ["-1", 0],
            TypeError: [[], None, {}],
            ValueError: ["a"],
        }

        instance = MagicMock()

        for error, values in invalid_values_by_error.items():
            with self.subTest(values):
                for value in values:
                    with self.subTest(value), self.assertRaises(error):
                        instance.value = value

                        # noinspection PyCallByClass
                        BaseConfiguration._validate_value(instance)

    def test_validate_charge_value_1(self):
        """
        Dado:
            - uma coleção de valores válidos
            - uma instância qualquer
                que tenha o VALID_CHARGE_TYPES
        Quando:
            - for chamado Configuration._validate_charge_type(instance) para cada valor
                com o valor estando na instância
        Então:
            - N/A
        """
        valid_values = {
            BaseConfiguration.PERCENTAGE,
            BaseConfiguration.DAILY_PERCENTAGE,
        }

        instance = MagicMock(VALID_CHARGE_TYPES=valid_values)

        for value in valid_values:
            instance.charge_type = value

            # noinspection PyCallByClass
            BaseConfiguration._validate_charge_type(instance)

    def test_validate_charge_value_2(self):
        """
        Dado:
            - uma lista de valores inválidos
            - uma instância qualquer
                que tenha o VALID_CHARGE_TYPES
        Quando:
            - for chamado Configuration._validate_charge_type(instance) para cada valor
                com o valor estando na instância
        Então:
            - deve ser lançado um FieldError para cada
        """
        invalid_values = [
            "foo",
            1,
            None,
            "a",
            "-1",
            BaseConfiguration.PERCENTAGE,
            BaseConfiguration.FIXED,
            BaseConfiguration.DAILY_FIXED,
        ]

        instance = MagicMock(
            VALID_CHARGE_TYPES={
                BaseConfiguration.DAILY_PERCENTAGE,
                BaseConfiguration.MONTHLY_PERCENTAGE,
            }
        )

        for value in invalid_values:
            instance.charge_type = value

            with self.assertRaises(FieldError):
                # noinspection PyCallByClass
                BaseConfiguration._validate_charge_type(instance)


class InterestConfigurationTestCase(TestCase):
    def test_valid_charge_types(self):
        expected = {
            BaseConfiguration.DAILY_FIXED,
            BaseConfiguration.DAILY_PERCENTAGE,
            BaseConfiguration.MONTHLY_PERCENTAGE,
        }

        result = InterestConfiguration.VALID_CHARGE_TYPES

        self.assertEqual(result, expected)


class FineConfigurationTestCase(TestCase):
    def test_valid_charge_types(self):
        expected = {
            BaseConfiguration.PERCENTAGE,
            BaseConfiguration.FIXED,
        }

        result = FineConfiguration.VALID_CHARGE_TYPES

        self.assertEqual(result, expected)


class DiscountConfigurationTestCase(TestCase):
    def test_valid_charge_types(self):
        expected = {
            BaseConfiguration.PERCENTAGE,
            BaseConfiguration.FIXED,
        }

        result = DiscountConfiguration.VALID_CHARGE_TYPES

        self.assertEqual(result, expected)

    def test_validate_date_1(self):
        """
        Dado:
            - uma lista de valores válidos
            - uma instância qualquer
        Quando:
            - for chamado Configuration._validate_date(instance) para cada valor
                com o valor estando na instância
        Então:
            - N/A
        """
        valid_values = ["2020-08-28", "0000-18-00", "2020-12-20"]

        instance = MagicMock()

        for value in valid_values:
            with self.subTest(value):
                instance.date = value
                # noinspection PyCallByClass
                DiscountConfiguration._validate_date(instance)

    def test_validate_date_2(self):
        """
        Dado:
            - um mapeamento invalid_values_by_error de vários erros para listas de valores inválidos
                {
                    FieldError: ['-1', 0],
                    TypeError: [[], None, {}],
                    ValueError: ['a']
                }
            - uma instância qualquer
        Quando:
            - for chamado Configuration._validate_value(instance) para cada erro e valor
                com o valor estando na instância
        Então:
            - deve ser lançado o erro específico para cada valor
        """
        invalid_values_by_error = {
            FieldError: ["-1", "a"],
            TypeError: [0, {}, [], None]
        }

        instance = MagicMock()

        for error, values in invalid_values_by_error.items():
            with self.subTest(values):
                for value in values:
                    with self.subTest(value), self.assertRaises(error):
                        instance.date = value

                        # noinspection PyCallByClass
                        DiscountConfiguration._validate_date(instance)
