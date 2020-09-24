from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import validate_obj_attr_type
from imopay_wrapper.exceptions import FieldError


class ValidateObjAttrTypeTestCase(TestCase):
    def test_1(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
        Quando:
            - for chamado validate_obj_attr_type(obj, "foo", str)
        Então:
            - N/A
        """
        obj = MagicMock(foo="bar")

        validate_obj_attr_type(obj, "foo", str)

    def test_2(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
        Quando:
            - for chamado validate_obj_attr_type(obj, "foo", int)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro deve estar correto
        """
        obj = MagicMock(foo="bar")

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_type(obj, "foo", int)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não é do tipo", ctx.exception.reason)
        self.assertIn(str(int), ctx.exception.reason)
