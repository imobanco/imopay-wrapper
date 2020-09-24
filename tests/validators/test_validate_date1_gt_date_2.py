from unittest import TestCase

from imopay_wrapper.validators import validate_date_1_gt_date_2
from imopay_wrapper.exceptions import FieldError


class ValidateDate1gtDate2TestCase(TestCase):
    def test_1(self):
        """
        Dado:
            - uma data válida d1 "2020-08-29"
            - uma data válida d2 "2020-08-28"
            - um nome de atributo qualquer "foo"
        Quando:
            - for chamado validate_date_1_gt_date_2("foo", d1, d2)
        Então:
            - N/A
        """
        d1 = "2020-08-29"
        d2 = "2020-08-28"
        validate_date_1_gt_date_2("foo", d1, d2)

    def test_2(self):
        """
        Dado:
            - uma data válida d1 "2020-08-28"
            - uma data válida d2 "2020-08-29"
            - um nome de atributo qualquer "foo"
        Quando:
            - for chamado validate_date_1_gt_date_2("foo", d1, d2)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro deve ser correto
        """
        d1 = "2020-08-28"
        d2 = "2020-08-29"

        with self.assertRaises(FieldError) as ctx:
            validate_date_1_gt_date_2("foo", d1, d2)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(
            f"{d1} não é estritamente maior do que {d2}", ctx.exception.reason
        )

    def test_3(self):
        """
        Dado:
            - uma data válida d1 "2020-08-28"
            - uma data válida d2 "2020-08-29"
            - um nome de atributo qualquer "foo"
        Quando:
            - for chamado validate_date_1_gt_date_2("foo", d1, d2, allow_equal=True)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro deve ser correto
        """
        d1 = "2020-08-28"
        d2 = "2020-08-29"

        with self.assertRaises(FieldError) as ctx:
            validate_date_1_gt_date_2("foo", d1, d2, allow_equal=True)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(f"{d1} não é igual ou maior do que {d2}", ctx.exception.reason)

    def test_4(self):
        """
        Dado:
            - uma data válida d1 "2020-08-28"
            - uma data válida d2 "2020-08-28"
            - um nome de atributo qualquer "foo"
        Quando:
            - for chamado validate_date_1_gt_date_2("foo", d1, d2)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro deve ser correto
        """
        d1 = "2020-08-28"
        d2 = "2020-08-28"

        with self.assertRaises(FieldError) as ctx:
            validate_date_1_gt_date_2("foo", d1, d2)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(
            f"{d1} não é estritamente maior do que {d2}", ctx.exception.reason
        )

    def test_5(self):
        """
        Dado:
            - uma data válida d1 "2020-08-28"
            - uma data válida d2 "2020-08-28"
            - um nome de atributo qualquer "foo"
        Quando:
            - for chamado validate_date_1_gt_date_2("foo", d1, d2, allow_equal=True)
        Então:
            - N/A
        """
        d1 = "2020-08-28"
        d2 = "2020-08-28"

        validate_date_1_gt_date_2("foo", d1, d2, allow_equal=True)
