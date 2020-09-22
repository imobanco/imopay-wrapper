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
        """
        Dado:
            - N/A
        Quando:
            - for chamado BaseImopayObj()
        Então:
            - BaseImopayObj._BaseImopayObj__run_validators deve ter sido chamado
            - BaseImopayObj._init_nested_fields deve ter sido chamado
        """
        with patch(
            "imopay_wrapper.models.base.BaseImopayObj._BaseImopayObj__run_validators"
        ) as mocked_run_validators, patch(
            "imopay_wrapper.models.base.BaseImopayObj._init_nested_fields"
        ) as mocked_init_nested_fields:
            BaseImopayObj()

        mocked_run_validators.assert_called_once_with()
        mocked_init_nested_fields.assert_called_once_with()

    def test_get_validation_methods_1(self):
        """
        Dado:
            - Uma classe custom que herde do BaseImopayObj
                e ela tenha um método FORA do padrão _validate
            - Um objeto dessa classe
        Quando:
            - for chamado obj._BaseImopayObj__get_validation_methods()
        Então:
            - o resultado deve ser uma lista vazia
        """

        class CustomClass(BaseImopayObj):
            foo: str

            def _valida_foo(self):
                pass

        obj = CustomClass()

        expected = []

        result = obj._BaseImopayObj__get_validation_methods()

        self.assertEqual(result, expected)

    def test_get_validation_methods_2(self):
        """
        Dado:
            - Uma classe custom que herde do BaseImopayObj
                e ela tenha um método no padrão _validate
            - Um objeto dessa classe
        Quando:
            - for chamado obj._BaseImopayObj__get_validation_methods()
        Então:
            - o resultado deve possuir uma entrada
            - essa entrada deve ser um "chamável"
        """

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
        """
        Dado:
            - um objeto obj BaseImopayObj
            - um método qualquer mocked_validator_method
            - BaseImopayObj._BaseImopayObj__get_validation_methods retornando
                [mocked_validator_method]
        Quando:
            - for chamado obj._BaseImopayObj__run_validators()
        Então:
            - mocked_validator_method deve ter sido chamado uma vez
        """
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
        """
        Dado:
            - um objeto obj BaseImopayObj
            - um erro er1 FieldError("foo", "bar")
            - um método qualquer mocked_validator_method que levante o error
            - BaseImopayObj._BaseImopayObj__get_validation_methods retornando
                [mocked_validator_method]
        Quando:
            - for chamado obj._BaseImopayObj__run_validators()
        Então:
            - deve ser lançado um erro er2 ValidationError
            - o er1 deve estar presente na lista de erros de er2
        """
        obj = BaseImopayObj()

        er1 = FieldError("foo", "bar")

        mocked_validator_method = MagicMock(side_effect=er1)

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj."
            "_BaseImopayObj__get_validation_methods"
        ) as mocked_get_validation_methods:
            mocked_get_validation_methods.return_value = [mocked_validator_method]

            with self.assertRaises(ValidationError) as ctx:
                obj._BaseImopayObj__run_validators()

        mocked_validator_method.assert_called_once_with()

        er2 = ctx.exception

        self.assertEqual(len(er2.errors), 1)
        self.assertEqual(er2.errors[0], er1)
