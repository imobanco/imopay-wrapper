from unittest import TestCase
from unittest.mock import MagicMock

from imopay_wrapper.validators import _get_value_from_attr_or_value


class GetValueTestCase(TestCase):
    def test_1(self):
        obj = MagicMock(foo="bar")

        expected = "bar"

        result = _get_value_from_attr_or_value(obj, "foo")

        self.assertEqual(result, expected)

    def test_2(self):
        obj = MagicMock(foo="bar")

        expected = "bar2"

        result = _get_value_from_attr_or_value(obj, "foo", value="bar2")

        self.assertEqual(result, expected)

    def test_3(self):
        obj = ''

        expected = None

        result = _get_value_from_attr_or_value(obj, "foo")

        self.assertEqual(result, expected)
