from unittest import TestCase

from imopay_wrapper.models.transaction import InvoiceConfigurations, Configuration


class InvoiceConfigurationsTestCase(TestCase):
    def test_1(self):
        t = InvoiceConfigurations.from_dict(
            {
                "fine": Configuration.from_dict(
                    {"value": 1, "type": "foo", "charge_type": "foo", "days": 0}
                )
            }
        )
        self.assertEqual(t.fine.value, 1)

    def test_2(self):
        t = InvoiceConfigurations.from_dict(
            {"fine": {"value": 1, "type": "foo", "charge_type": "foo", "days": 0}}
        )
        self.assertEqual(t.fine.value, 1)
