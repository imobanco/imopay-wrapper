from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import validate_obj_attr_regex
from imopay_wrapper.exceptions import FieldError
from imopay_wrapper.regex import date_regex


class ValidateObjAttrRegexTestCase(TestCase):
    def test_1(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="2020-08-20"
            - um regex de data
        Quando:
            - for chamado validate_obj_attr_regex(obj, "foo", date_regex)
        Então:
            - N/A
        """
        obj = MagicMock(foo="2020-08-20")

        validate_obj_attr_regex(obj, "foo", date_regex)

    def test_2(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
            - um regex de data
        Quando:
            - for chamado validate_obj_attr_regex(obj, "foo", date_regex)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro deve estar correto
        """
        obj = MagicMock(foo="bar")

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_regex(obj, "foo", date_regex)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não é do formato", ctx.exception.reason)
        self.assertIn(date_regex, ctx.exception.reason)
