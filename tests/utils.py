from unittest import TestCase
from unittest.mock import patch, PropertyMock


class LocalImopayTestCase(TestCase):
    def setUp(self):
        self.base_url_patcher = patch(
            "imopay_wrapper.wrapper.base.RequestsWrapper._base_url",
            new_callable=PropertyMock,
        )

        self.mocked_base_url = self.base_url_patcher.start()
        self.mocked_base_url.return_value = "http://localhost:8000"

        self.addCleanup(self.base_url_patcher.stop)
