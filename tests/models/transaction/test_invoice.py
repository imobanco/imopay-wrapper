from unittest import TestCase

from imopay_wrapper.models.transaction import Invoice, BaseConfiguration


class InvoiceTestCase(TestCase):
    def test_1(self):
        t = Invoice.from_dict(
            {
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
                }
            }
        )
        self.assertEqual(t.configurations.fine.value, 1)
        self.assertEqual(t.configurations.interest.value, 1)
        self.assertEqual(t.configurations.discounts[0].value, 1)
