from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import validate_obj_attr_in_collection
from imopay_wrapper.exceptions import FieldError


class ValidateObjAttrInCollectionTestCase(TestCase):
    def test_1(self):

        obj = MagicMock(foo="bar")

        collection = ["bar"]

        validate_obj_attr_in_collection(obj, "foo", collection)

    def test_2(self):

        obj = MagicMock()

        collection = ["bar"]

        validate_obj_attr_in_collection(obj, "foo", collection, value="bar")

    def test_3(self):

        obj = MagicMock(foo="bar")

        collection = [1]

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_in_collection(obj, "foo", collection)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não está na coleção", ctx.exception.reason)
        self.assertIn(str(collection), ctx.exception.reason)

    def test_4(self):

        obj = MagicMock()

        collection = [1]

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_in_collection(obj, "foo", collection, value="bar")

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não está na coleção", ctx.exception.reason)
        self.assertIn(str(collection), ctx.exception.reason)
