from unittest import TestCase
from unittest.mock import MagicMock

from ..utils import today, tomorrow, yesterday

from imopay_wrapper.validators import validate_date_isoformat
from imopay_wrapper.exceptions import FieldError


class ValidateDateIsoformatTestCase(TestCase):    
    def test_1(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo="2020-08-28"
        Quando:
            - for chamado validate_date_isoformat(obj, "foo")
        Então:
            - N/A
        """
        obj = MagicMock(foo="2020-08-28")

        validate_date_isoformat(obj, "foo")

    def test_2(self):
        """
        Dado:
            - um mapeamento de erros para uma lista de valores inválidos
                invalid_mapping_error_values = {
                    ValueError: ["28/08/2020", "abc"],
                    TypeError: [1, None, {}]
                }
            - um objeto qualquer
        Quando:
            - for chamado validate_date_isoformat(obj, "foo") para cada erro e valor
                com o valor estando na instância
        Então:
            - deve ser lançado o erro específico para cada valor
        """
        invalid_mapping_error_values = {
            ValueError: ["28/08/2020", "abc"],
            TypeError: [1, None, {}]
        }

        obj = MagicMock()

        for error, values in invalid_mapping_error_values.items():
            for value in values:
                obj.foo = value
                with self.subTest(value), self.assertRaises(error):
                    validate_date_isoformat(obj, "foo")

    def test_3(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de amanhã
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", future=True)
        Então:
            - N/A
        """
        obj = MagicMock(foo=tomorrow())

        validate_date_isoformat(obj, "foo", future=True)

    def test_4(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de hoje
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", future=True, allow_today=True)
        Então:
            - N/A
        """
        obj = MagicMock(foo=today())

        validate_date_isoformat(obj, "foo", future=True, allow_today=True)

    def test_5(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de hoje
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", future=True, allow_today=False)
        Então:
            - deve ser lançado um FieldError
            - o texto do erro deve ser correto
        """
        obj = MagicMock(foo=today())

        with self.assertRaises(FieldError) as ctx:
            validate_date_isoformat(obj, "foo", future=True, allow_today=False)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(f"{obj.foo} não é uma data do futuro!", ctx.exception.reason)

    def test_6(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de ontem
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", future=True)
        Então:
            - deve ser lançado um FieldError
            - o texto da exceção deve ser correto
        """
        obj = MagicMock(foo=yesterday())

        with self.assertRaises(FieldError) as ctx:
            validate_date_isoformat(obj, "foo", future=True)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(f"{obj.foo} não é uma data do futuro!", ctx.exception.reason)

    def test_7(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de ontem
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", past=True)
        Então:
            - N/A
        """
        obj = MagicMock(foo=yesterday())

        validate_date_isoformat(obj, "foo", past=True)

    def test_8(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de hoje
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", past=True, allow_today=True)
        Então:
            - N/A
        """
        obj = MagicMock(foo=today())

        validate_date_isoformat(obj, "foo", past=True, allow_today=True)

    def test_9(self):
        """
        Dado:
            - um objeto obj qualquer que tenha foo com a data de hoje
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", past=True, allow_today=False)
        Então:
            - deve ser lançado um FieldError
            - o texto da exceção deve ser correto
        """
        obj = MagicMock(foo=today())

        with self.assertRaises(FieldError) as ctx:
            validate_date_isoformat(obj, "foo", past=True, allow_today=False)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(f"{obj.foo} não é uma data do passado!", ctx.exception.reason)

    def test_10(self):
        """
        Dado:
            - uma data de amanhã
            - um objeto obj qualquer que tenha foo com a data de amanhã
        Quando:
            - for chamado validate_date_isoformat(obj, "foo", past=True)
        Então:
            - deve ser lançado um FieldError
            - o texto da exceção deve ser correto
        """
        obj = MagicMock(foo=tomorrow())

        with self.assertRaises(FieldError) as ctx:
            validate_date_isoformat(obj, "foo", past=True)

        self.assertEqual(ctx.exception.name, "foo")
        self.assertIn(f"{obj.foo} não é uma data do passado!", ctx.exception.reason)

    def test_11(self):

        with self.assertRaises(ValueError) as ctx:
            validate_date_isoformat("", "", future=True, past=True)

        self.assertIn("Não se pode verificar se é uma data futura e passada ao mesmo tempo!", str(ctx.exception))
