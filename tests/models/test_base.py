from unittest import TestCase
from unittest.mock import patch, MagicMock
from dataclasses import dataclass

from imopay_wrapper.models.base import BaseImopayObj
from imopay_wrapper.exceptions import ValidationError, FieldError


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

    def test_post_init(self):

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj._BaseImopayObj__run_validators"
        ) as mocked_run_validators, patch(
            "imopay_wrapper.models.base.BaseImopayObj._init_nested_fields"
        ) as mocked_init_nested_fields:
            BaseImopayObj()

        mocked_run_validators.assert_called_once_with()
        mocked_init_nested_fields.assert_called_once_with()

    def test_get_validation_methods_1(self):
        obj = BaseImopayObj()

        expected = []

        result = obj._BaseImopayObj__get_validation_methods()

        self.assertEqual(result, expected)

    def test_get_validation_methods_2(self):
        class CustomClass(BaseImopayObj):
            foo: str

            def _validate_foo(self):
                pass

        obj = CustomClass()

        result = obj._BaseImopayObj__get_validation_methods()

        self.assertEqual(len(result), 1)

        for item in result:
            with self.subTest(item):
                self.assertTrue(callable(item))

    def test_run_validators_1(self):
        obj = BaseImopayObj()

        mocked_validator_method = MagicMock()

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj."
            "_BaseImopayObj__get_validation_methods"
        ) as mocked_get_validation_methods:
            mocked_get_validation_methods.return_value = [mocked_validator_method]

            obj._BaseImopayObj__run_validators()

        mocked_validator_method.assert_called_once_with()

    def test_run_validators_2(self):
        obj = BaseImopayObj()

        error = FieldError("foo", "bar")

        mocked_validator_method = MagicMock(side_effect=error)

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj."
            "_BaseImopayObj__get_validation_methods"
        ) as mocked_get_validation_methods:
            mocked_get_validation_methods.return_value = [mocked_validator_method]

            with self.assertRaises(ValidationError) as ctx:
                obj._BaseImopayObj__run_validators()

        mocked_validator_method.assert_called_once_with()

        self.assertEqual(len(ctx.exception.errors), 1)
        self.assertEqual(ctx.exception.errors[0], error)
