from unittest import TestCase

from imopay_wrapper.models.transaction import InvoiceConfigurations, BaseConfiguration


class InvoiceConfigurationsTestCase(TestCase):
    def test_1(self):
        t = InvoiceConfigurations.from_dict(
            {"fine": {"value": 1, "charge_type": BaseConfiguration.PERCENTAGE}}
        )
        self.assertEqual(t.fine.value, 1)

    def test_2(self):
        t = InvoiceConfigurations.from_dict(
            {"interest": {"value": 1, "charge_type": BaseConfiguration.DAILY_FIXED}}
        )
        self.assertEqual(t.interest.value, 1)

    def test_3(self):
        t = InvoiceConfigurations.from_dict(
            {
                "discounts": [
                    {
                        "value": 1,
                        "charge_type": BaseConfiguration.FIXED,
                        "date": "2020-08-28",
                    }
                ]
            }
        )
        self.assertEqual(t.discounts[0].value, 1)
