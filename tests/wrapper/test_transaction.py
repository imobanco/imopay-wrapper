from unittest.mock import patch

from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper


class TransactionWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().transaction

    def test_action(self):
        self.assertEqual(self.client.action, "transactions")

    def test_create_invoice(self):
        expected_data = {
            "payer": "1",
            "receiver": "2",
            "reference_id": "3",
            "amount": 4,
            "description": "5",
            "payment_method": {
                "expiration_date": "6",
                "limit_date": "7",
                "configurations": {
                    "fine": {
                        "type": "8",
                        "charge_type": "9",
                        "value": "10",
                        "days": "11",
                    },
                    "interest": {
                        "type": "12",
                        "charge_type": "13",
                        "value": "14",
                        "days": "15",
                    },
                    "discounts": [
                        {"type": "16", "charge_type": "17", "value": "18", "days": "19"}
                    ],
                },
            },
        }

        expected_url = self.client._construct_url(
            action=self.client.action, subaction="create_invoice"
        )

        with patch(
            "imopay_wrapper.wrapper.base.BaseImopayWrapper._post"
        ) as mocked_post:
            self.client.create_invoice(
                {
                    "payer": "1",
                    "receiver": "2",
                    "reference_id": "3",
                    "amount": "4",
                    "description": "5",
                    "payment_method": {
                        "expiration_date": "6",
                        "limit_date": "7",
                        "configurations": {
                            "fine": {
                                "type": "8",
                                "charge_type": "9",
                                "value": "10",
                                "days": "11",
                            },
                            "interest": {
                                "type": "12",
                                "charge_type": "13",
                                "value": "14",
                                "days": "15",
                            },
                            "discounts": [
                                {
                                    "type": "16",
                                    "charge_type": "17",
                                    "value": "18",
                                    "days": "19",
                                }
                            ],
                        },
                    },
                }
            )

        mocked_post.assert_called_once_with(expected_url, expected_data)
