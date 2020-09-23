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

    def test_validation_method_pattern(self):
        expected = "_validate"

        result = BaseImopayObj.VALIDATION_METHOD_PATTERN

        self.assertEqual(result, expected)

    def test_is_empty_value(self):
        self.assertTrue(BaseImopayObj._BaseImopayObj__is_empty_value(""))

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

        @dataclass
        class CustomClass(BaseImopayObj):
            foo: str

            def _validate_foo(self):
                pass

        obj = CustomClass.from_dict(None)

        result = obj._BaseImopayObj__get_validation_methods()

        self.assertEqual(len(result), 1)

        for item in result:
            with self.subTest(item):
                self.assertTrue(callable(item))

    def test_get_attr_name_from_method_1(self):
        """
        Dado:
            - um método com
                __name__="_validate_foo"
        Quando:
            - for chamado BaseImopayObj._BaseImopayObj__get_attr_name_from_method(method)  # noqa
        Então:
            - o resultado deve ser "foo"
        """
        method = MagicMock(__name__="_validate_foo")

        expected = "foo"

        result = BaseImopayObj._BaseImopayObj__get_attr_name_from_method(method)

        self.assertEqual(result, expected)

    def test_get_field_1(self):
        """
        Dado:
            - um nome de campo field_name 'foo'
            - um campo qualquer mocked_field
            - um objeto qualquer obj que tenha o campo field_name: mocked_field
        Quando:
            - for chamado BaseImopayObj._BaseImopayObj__get_field(obj, field_name)
        Então:
            - o resultado deve ser mocked_field
        """
        field_name = "foo"

        mocked_field = MagicMock()

        obj = MagicMock(
            _BaseImopayObj__get_fields=MagicMock(return_value={field_name: mocked_field})
        )

        expected = mocked_field

        result = BaseImopayObj._BaseImopayObj__get_field(obj, field_name)

        self.assertEqual(result, expected)

    def test_get_field_2(self):
        """
        Dado:
            - um nome de campo field_name 'foo'
            - um campo qualquer mocked_field
            - um objeto qualquer obj que tenha o campo 'bar': mocked_field
        Quando:
            - for chamado BaseImopayObj._BaseImopayObj__get_field(obj, name)
        Então:
            - deve ser lançado um AttributeError
        """
        field_name = "foo"

        mocked_field = MagicMock()

        obj = MagicMock(
            _BaseImopayObj__get_fields=MagicMock(return_value={"bar": mocked_field})
        )

        with self.assertRaises(AttributeError):
            BaseImopayObj._BaseImopayObj__get_field(obj, field_name)

    def test_is_field_optional_1(self):
        """
        Dado:
            - um campo qualquer mocked_field optional=True
        Quando:
            - quando for chamado BaseImopayObj._BaseImopayObj__is_field_optional(mocked_field)  # noqa
        Então:
            - o resultado deve ser True
        """
        mocked_field = MagicMock(optional=True)

        expected = True

        result = BaseImopayObj._BaseImopayObj__is_field_optional(mocked_field)

        self.assertEqual(result, expected)

    def test_is_field_optional_2(self):
        """
        Dado:
            - um campo qualquer mocked_field optional=False
        Quando:
            - quando for chamado BaseImopayObj._BaseImopayObj__is_field_optional(mocked_field)  # noqa
        Então:
            - o resultado deve ser False
        """
        mocked_field = MagicMock(optional=False)

        expected = False

        result = BaseImopayObj._BaseImopayObj__is_field_optional(mocked_field)

        self.assertEqual(result, expected)

    def test_is_field_optional_3(self):
        """
        Dado:
            - um campo qualquer mocked_field que não tenha o atributo optional
        Quando:
            - quando for chamado BaseImopayObj._BaseImopayObj__is_field_optional(mocked_field)  # noqa
        Então:
            - o resultado deve ser False
        """
        expected = False

        mocked_field = ""

        result = BaseImopayObj._BaseImopayObj__is_field_optional(mocked_field)

        self.assertEqual(result, expected)

    def test_run_validators_1(self):
        """
        Dado:
            - um objeto obj BaseImopayObj
            - um método qualquer mocked_validator_method
                com __name__="_validate_foo"
            - BaseImopayObj._BaseImopayObj__get_validation_methods retornando
                [mocked_validator_method]
            - existe o campo 'foo' em obj com optional=False
        Quando:
            - for chamado obj._BaseImopayObj__run_validators()
        Então:
            - mocked_validator_method deve ter sido chamado uma vez
            - BaseImopayObj._BaseImopayObj__get_field('foo') deve
                ter sido chamado uma vez
        """
        obj = BaseImopayObj()

        mocked_validator_method = MagicMock(__name__="_validate_foo")

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj."
            "_BaseImopayObj__get_validation_methods"
        ) as mocked_get_validation_methods, patch(
            "imopay_wrapper.models.base.BaseImopayObj." "_BaseImopayObj__get_field"
        ) as mocked_get_field:
            mocked_get_field.return_value = MagicMock(optional=False)

            mocked_get_validation_methods.return_value = [mocked_validator_method]

            obj._BaseImopayObj__run_validators()

        mocked_validator_method.assert_called_once_with()
        mocked_get_field.assert_called_once_with("foo")

    def test_run_validators_2(self):
        """
        Dado:
            - um objeto obj BaseImopayObj
            - um erro er1 FieldError("foo", "bar")
            - um método qualquer mocked_validator_method que levante o error e
                com __name__="_validate_foo"
            - BaseImopayObj._BaseImopayObj__get_validation_methods retornando
                [mocked_validator_method]
            - existe o campo 'foo' em obj com optional=False
        Quando:
            - for chamado obj._BaseImopayObj__run_validators()
        Então:
            - mocked_validator_method deve ter sido chamado uma vez
            - BaseImopayObj._BaseImopayObj__get_field('foo') deve
                ter sido chamado uma vez
            - deve ser lançado um erro er2 ValidationError
            - o er1 deve estar presente na lista de erros de er2
        """
        obj = BaseImopayObj()

        er1 = FieldError("foo", "bar")

        mocked_validator_method = MagicMock(side_effect=er1, __name__="_validate_foo")

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj."
            "_BaseImopayObj__get_validation_methods"
        ) as mocked_get_validation_methods, patch(
            "imopay_wrapper.models.base.BaseImopayObj." "_BaseImopayObj__get_field"
        ) as mocked_get_field:
            mocked_get_field.return_value = MagicMock(optional=False)

            mocked_get_validation_methods.return_value = [mocked_validator_method]

            with self.assertRaises(ValidationError) as ctx:
                obj._BaseImopayObj__run_validators()

        mocked_validator_method.assert_called_once_with()
        mocked_get_field.assert_called_once_with("foo")

        er2 = ctx.exception

        self.assertEqual(len(er2.errors), 1)
        self.assertEqual(er2.errors[0], er1)

    def test_run_validators_3(self):
        """
        Dado:
            - um objeto obj BaseImopayObj
            - um erro er1 FieldError("foo", "bar")
            - um método qualquer mocked_validator_method que levante o error e
                com __name__="_validate_foo"
            - BaseImopayObj._BaseImopayObj__get_validation_methods retornando
                [mocked_validator_method]
            - existe o campo 'foo' em obj com optional=True
        Quando:
            - for chamado obj._BaseImopayObj__run_validators()
        Então:
            - mocked_validator_method deve ter sido chamado uma vez
            - BaseImopayObj._BaseImopayObj__get_field('foo') deve
                ter sido chamado uma vez
        """
        obj = BaseImopayObj()

        er1 = FieldError("foo", "bar")

        mocked_validator_method = MagicMock(side_effect=er1, __name__="_validate_foo")

        with patch(
            "imopay_wrapper.models.base.BaseImopayObj."
            "_BaseImopayObj__get_validation_methods"
        ) as mocked_get_validation_methods, patch(
            "imopay_wrapper.models.base.BaseImopayObj." "_BaseImopayObj__get_field"
        ) as mocked_get_field:
            mocked_get_field.return_value = MagicMock(optional=True)

            mocked_get_validation_methods.return_value = [mocked_validator_method]

            obj._BaseImopayObj__run_validators()

        mocked_validator_method.assert_called_once_with()
        mocked_get_field.assert_called_once_with("foo")
