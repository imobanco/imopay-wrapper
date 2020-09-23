from unittest.mock import patch

from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.models.transaction import BaseConfiguration


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
                "expiration_date": "2020-08-28",
                "limit_date": "2020-08-28",
                "configurations": {
                    "fine": {
                        "value": 1,
                        "charge_type": BaseConfiguration.FIXED,
                    },
                    "interest": {
                        "value": 1,
                        "charge_type": BaseConfiguration.DAILY_FIXED,
                    },
                    "discounts": [
                        {
                            "value": 1,
                            "charge_type": BaseConfiguration.FIXED,
                            "date": "2020-08-28",
                        }
                    ],
                },
            },
        }

        expected_url = self.client._construct_url(
            action=self.client.action, subaction="create_invoice_transaction"
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
                        "expiration_date": "2020-08-28",
                        "limit_date": "2020-08-28",
                        "configurations": {
                            "fine": {
                                "value": 1,
                                "charge_type": BaseConfiguration.FIXED,
                            },
                            "interest": {
                                "value": 1,
                                "charge_type": BaseConfiguration.DAILY_FIXED,
                            },
                            "discounts": [
                                {
                                    "value": 1,
                                    "charge_type": BaseConfiguration.FIXED,
                                    "date": "2020-08-28",
                                }
                            ],
                        },
                    },
                }
            )

        mocked_post.assert_called_once_with(expected_url, expected_data)
