from unittest.mock import patch, PropertyMock

from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.models.address import Address


class PersonWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().address

    def test_model(self):
        self.assertEqual(self.client.model, Address)

    def test_action(self):
        self.assertEqual(self.client.action, "addresses")

    def test_create(self):
        with patch(
            "imopay_wrapper.wrapper.address.AddressWrapper.model",
            new_callable=PropertyMock,
        ) as mocked_model, patch(
            "imopay_wrapper.wrapper.address.AddressWrapper.action",
            new_callable=PropertyMock,
        ) as mocked_action, patch(
            "imopay_wrapper.wrapper.address.AddressWrapper._post"
        ) as mocked_post:
            self.client.create({})

        mocked_model.assert_called_once()

        mocked_action.assert_called_once()

        mocked_post.assert_called_once_with(
            self.client._construct_url(action=mocked_action.return_value, subaction='create_by_name_and_uf'),
            mocked_model.return_value.return_value.to_dict.return_value,
        )
