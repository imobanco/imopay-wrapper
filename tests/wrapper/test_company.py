from unittest.mock import patch

from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.models.company import Company


class CompanyWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().company

    def test_model(self):
        self.assertEqual(self.client.model, Company)

    def test_action(self):
        self.assertEqual(self.client.action, "companies")

    def test_search(self):
        cnpj = "foo"

        expected_data = {"cnpj": cnpj}

        expected_url = self.client._construct_url(
            action=self.client.action, subaction="search"
        )

        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._post"
        ) as mocked_post:
            self.client.search(cnpj)

        mocked_post.assert_called_once_with(expected_url, expected_data)
