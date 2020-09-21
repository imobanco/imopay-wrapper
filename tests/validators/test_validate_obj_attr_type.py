from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import validate_obj_attr_type
from imopay_wrapper.exceptions import FieldError


class ValidateObjAttrTypeTestCase(TestCase):
    def test_1(self):

        obj = MagicMock(foo="bar")

        validate_obj_attr_type(obj, "foo", str)

    def test_2(self):

        obj = MagicMock()

        validate_obj_attr_type(obj, "foo", str, value="bar")

    def test_3(self):

        obj = MagicMock(foo="bar")

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_type(obj, "foo", int)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não é do tipo", ctx.exception.reason)
        self.assertIn(str(int), ctx.exception.reason)

    def test_4(self):

        obj = MagicMock()

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_type(obj, "foo", int, value="bar")

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não é do tipo", ctx.exception.reason)
        self.assertIn(str(int), ctx.exception.reason)
