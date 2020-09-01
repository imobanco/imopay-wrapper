from unittest import TestCase

from imopay_wrapper.models.transaction import InvoiceTransaction


class InvoiceTransactionTestCase(TestCase):
    def test_1(self):
        t = InvoiceTransaction.from_dict(
            {
                "payment_method": {
                    "configurations": {
                        "fine": {
                            "value": 1,
                            "type": "foo",
                            "charge_type": "foo",
                            "days": 0
                        }
                    }
                }
            }
        )
        self.assertEqual(t.payment_method.configurations.fine.value, 1)
