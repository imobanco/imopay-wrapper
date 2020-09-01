from unittest import TestCase

from imopay_wrapper.models.transaction import Invoice


class InvoiceTestCase(TestCase):
    def test_1(self):
        t = Invoice.from_dict(
            {
                "configurations": {
                    "fine": {"value": 1, "type": "foo", "charge_type": "foo", "days": 0}
                }
            }
        )
        self.assertEqual(t.configurations.fine.value, 1)
