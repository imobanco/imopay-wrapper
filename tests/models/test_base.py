from unittest import TestCase
from dataclasses import dataclass

from imopay_wrapper.models.base import BaseImopayObj


class BaseImopayObjTestCase(TestCase):
    def setUp(self):
        @dataclass
        class CustomClass(BaseImopayObj):
            required: str
            non_required: str = ""

        self.custom_class = CustomClass

    def test_is_empty_value(self):
        self.assertTrue(BaseImopayObj.is_empty_value(""))

    def test_to_dict_1(self):
        o1 = self.custom_class(required="value")

        self.assertEqual(o1.required, "value")
        self.assertEqual(o1.non_required, "")

        expected = {"required": "value"}

        retult = o1.to_dict()

        self.assertEqual(retult, expected)

    def test_to_dict_2(self):
        o1 = self.custom_class(required="1", non_required="2")

        self.assertEqual(o1.required, "1")
        self.assertEqual(o1.non_required, "2")

        expected = {"required": "1", "non_required": "2"}

        retult = o1.to_dict()

        self.assertEqual(retult, expected)

    def test_to_dict_3(self):
        o1 = self.custom_class(required=None, non_required="2")

        self.assertEqual(o1.required, None)
        self.assertEqual(o1.non_required, "2")

        expected = {"non_required": "2"}

        retult = o1.to_dict()

        self.assertEqual(retult, expected)

    def test_from_dict(self):
        data = {"non_required": "2"}

        o1 = self.custom_class.from_dict(data)

        self.assertEqual(o1.required, None)
        self.assertEqual(o1.non_required, "2")
