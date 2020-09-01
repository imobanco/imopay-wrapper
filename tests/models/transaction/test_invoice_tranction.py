from unittest import TestCase

from imopay_wrapper.models.transaction import InvoiceTransaction, BaseTransaction


class InvoiceTransactionTestCase(TestCase):
    def test_0(self):
        expected = set(BaseTransaction.get_fields().keys())

        result = set(InvoiceTransaction.get_fields().keys())

        for item in expected:
            with self.subTest(item):
                self.assertIn(item, result)

    def test_1(self):
        t = InvoiceTransaction.from_dict({})
        self.assertEqual(t.payer, None)

    def test_2(self):
        t = InvoiceTransaction.from_dict(
            {
                "payment_method": {
                    "configurations": {
                        "fine": {
                            "value": 1,
                            "type": "foo",
                            "charge_type": "foo",
                            "days": 0,
                        }
                    }
                }
            }
        )
        self.assertEqual(t.payment_method.configurations.fine.value, 1)
