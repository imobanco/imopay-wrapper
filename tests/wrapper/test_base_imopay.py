from unittest import TestCase
from unittest.mock import patch, PropertyMock

from imopay_wrapper.wrapper.base import (
    BaseImopayWrapper,
    CreateMixin,
    DestroyMixin,
    UpdateMixin,
    RetrieveMixin,
)


class BaseImopayWrapperTestCase(TestCase):
    def setUp(self):
        self.client = type(
            "A",
            (
                BaseImopayWrapper,
                CreateMixin,
                DestroyMixin,
                UpdateMixin,
                RetrieveMixin,
            ),
            {},
        )()

    def test_model(self):
        with self.assertRaises(NotImplementedError):
            self.client.model()

    def test_action(self):
        with self.assertRaises(NotImplementedError):
            self.client.action()

    def test_create(self):
        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.model",
            new_callable=PropertyMock,
        ) as mocked_model, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.action",
            new_callable=PropertyMock,
        ) as mocked_action, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._post"
        ) as mocked_post:
            self.client.create({})

        mocked_model.assert_called_once()

        mocked_action.assert_called_once()

        mocked_post.assert_called_once_with(
            self.client._construct_url(action=mocked_action.return_value),
            mocked_model.return_value.return_value.to_dict.return_value,
        )

    def test_destroy(self):
        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.model",
            new_callable=PropertyMock,
        ) as mocked_model, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.action",
            new_callable=PropertyMock,
        ) as mocked_action, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._delete"
        ) as mocked_delete:
            self.client.destroy("1")

        mocked_model.assert_not_called()

        mocked_action.assert_called_once()

        mocked_delete.assert_called_once_with(
            self.client._construct_url(
                action=mocked_action.return_value, identifier="1"
            )
        )

    def test_update(self):
        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.model",
            new_callable=PropertyMock,
        ) as mocked_model, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.action",
            new_callable=PropertyMock,
        ) as mocked_action, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._patch"
        ) as mocked_patch:
            self.client.update("1", {})

        mocked_model.assert_called_once()

        mocked_action.assert_called_once()

        mocked_patch.assert_called_once_with(
            self.client._construct_url(
                action=mocked_action.return_value, identifier="1"
            ),
            mocked_model.return_value.from_dict.return_value.to_dict.return_value,
        )

    def test_retrieve(self):
        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.model",
            new_callable=PropertyMock,
        ) as mocked_model, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper.action",
            new_callable=PropertyMock,
        ) as mocked_action, patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._get"
        ) as mocked_get:
            self.client.retrieve("1")

        mocked_model.assert_not_called()

        mocked_action.assert_called_once()

        mocked_get.assert_called_once_with(
            self.client._construct_url(
                action=mocked_action.return_value, identifier="1"
            )
        )
