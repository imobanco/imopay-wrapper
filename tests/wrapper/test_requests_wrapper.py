from unittest import TestCase
from unittest.mock import MagicMock
from json import JSONDecodeError

from requests import HTTPError

from imopay_wrapper.wrapper.base import RequestsWrapper


class RequestsWrapperTestCase(TestCase):
    def test_process_response_1(self):
        """
        Dado que:
            - existe uma resposta r1 mockada
        Quando essa resposta for processada
        Então:
            - r1.data deve ser r1.json.return_value
            - r1.reason deve ser r1.data
            - r1.raise_for_status deve ter sido chamado uma vez
        """
        r1 = MagicMock(json=MagicMock(), raise_for_status=MagicMock())

        RequestsWrapper._RequestsWrapper__process_response(r1)

        self.assertEqual(r1.data, r1.json.return_value)
        self.assertEqual(r1.reason, r1.data)

        r1.raise_for_status.assert_called_once()

    def test_process_response_2(self):
        """
        Dado que:
            - existe uma resposta r1 mockada de erro
        Quando essa resposta for processada
        Então:
            - deve ter sido lançado um HttpError
            - r1.data deve ser r1.json.return_value
            - r1.reason deve ser r1.data
            - r1.raise_for_status deve ter sido chamado uma vez
        """
        r1 = MagicMock(
            json=MagicMock(), raise_for_status=MagicMock(side_effect=HTTPError())
        )

        with self.assertRaises(HTTPError):
            RequestsWrapper._RequestsWrapper__process_response(r1)

        self.assertEqual(r1.data, r1.json.return_value)
        self.assertEqual(r1.reason, r1.data)

        r1.raise_for_status.assert_called_once()

    def test_process_response_3(self):
        """
        Dado que:
            - existe uma resposta r1 mockada com um body inválido (json)
        Quando essa resposta for processada
        Então:
            - r1.data deve ser {}
            - r1.reason deve ser r1.data
            - r1.raise_for_status deve ter sido chamado uma vez
        """
        r1 = MagicMock(
            json=MagicMock(side_effect=JSONDecodeError("", "", 1)),
            raise_for_status=MagicMock(),
        )

        RequestsWrapper._RequestsWrapper__process_response(r1)

        self.assertEqual(r1.data, {})
        self.assertEqual(r1.reason, r1.data)

        r1.raise_for_status.assert_called_once()
