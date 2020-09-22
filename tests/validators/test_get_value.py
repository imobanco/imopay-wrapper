from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import _get_value_from_attr_or_value


class GetValueTestCase(TestCase):
    def test_1(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
        Quando:
            - for chamado _get_value_from_attr_or_value(obj, "foo")
        Então:
            - deve ser retornado "bar"
        """
        obj = MagicMock(foo="bar")

        expected = "bar"

        result = _get_value_from_attr_or_value(obj, "foo")

        self.assertEqual(result, expected)

    def test_2(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="bar"
        Quando:
            - for chamado _get_value_from_attr_or_value(obj, "foo", value="bar2")
        Então:
            - deve ser retornado "bar2"
        """
        obj = MagicMock(foo="bar")

        expected = "bar2"

        result = _get_value_from_attr_or_value(obj, "foo", value="bar2")

        self.assertEqual(result, expected)

    def test_3(self):
        """
        Dado:
            - um objeto obj qualquer que não tenha foo="bar"
        Quando:
            - for chamado _get_value_from_attr_or_value(obj, "foo")
        Então:
            - deve ser retornado None
        """
        obj = ""

        expected = None

        result = _get_value_from_attr_or_value(obj, "foo")

        self.assertEqual(result, expected)
