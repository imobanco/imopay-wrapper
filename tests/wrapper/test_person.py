from unittest.mock import patch

from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.models.person import Person


class PersonWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().person

    def test_model(self):
        self.assertEqual(self.client.model, Person)

    def test_action(self):
        self.assertEqual(self.client.action, "persons")

    def test_search(self):
        cpf = "foo"

        expected_data = {"cpf": cpf}

        expected_url = self.client._construct_url(
            action=self.client.action, subaction="search"
        )

        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._post"
        ) as mocked_post:
            self.client.search(cpf)

        mocked_post.assert_called_once_with(expected_url, expected_data)
