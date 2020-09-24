from datetime import date, timedelta
from unittest import TestCase
from unittest.mock import patch, PropertyMock


def today():
    """
    Retorna a data de hoje no formado YYYY-mm-dd.

    https://strftime.org/
    """
    return date.today().strftime("%Y-%m-%d")


def tomorrow():
    """
    Retorna a data de amanhã no formado YYYY-mm-dd.

    https://strftime.org/
    """
    d = date.today()
    d += timedelta(days=1)
    return d.strftime("%Y-%m-%d")


def yesterday():
    """
    Retorna a data de ontem no formado YYYY-mm-dd.

    https://strftime.org/
    """
    d = date.today()
    d -= timedelta(days=1)
    return d.strftime("%Y-%m-%d")


class LocalImopayTestCase(TestCase):
    def setUp(self):
        self.base_url_patcher = patch(
            "imopay_wrapper.wrapper.base.RequestsWrapper._base_url",
            new_callable=PropertyMock,
        )

        self.mocked_base_url = self.base_url_patcher.start()
        self.mocked_base_url.return_value = "http://localhost:8000"

        self.addCleanup(self.base_url_patcher.stop)
