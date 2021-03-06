from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import validate_obj_attr_in_collection
from imopay_wrapper.exceptions import FieldError


class ValidateObjAttrInCollectionTestCase(TestCase):
    def test_1(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
            - uma coleção collection ["bar"]
        Quando:
            - for chamado validate_obj_attr_in_collection(obj, "foo", collection)
        Então:
            - N/A
        """
        obj = MagicMock(foo="bar")

        collection = ["bar"]

        validate_obj_attr_in_collection(obj, "foo", collection)

    def test_2(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
            - uma coleção collection [1]
        Quando:
            - for chamado validate_obj_attr_in_collection(obj, "foo", collection)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro lançado deve estar correto!
        """
        obj = MagicMock(foo="bar")

        collection = [1]

        with self.assertRaises(FieldError) as ctx:
            validate_obj_attr_in_collection(obj, "foo", collection)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn("bar não está na coleção", ctx.exception.reason)
        self.assertIn(str(collection), ctx.exception.reason)
