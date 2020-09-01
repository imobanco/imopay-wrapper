from unittest import TestCase

from imopay_wrapper.models.transaction import Configuration


class ConfigurationTestCase(TestCase):
    def test_1(self):
        t = Configuration.from_dict(
            {
                "value": 1,
                "type": "foo",
                "charge_type": "foo",
                "days": 0
            }
        )
        self.assertEqual(t.value, 1)
        self.assertEqual(t.type, 'foo')
        self.assertEqual(t.charge_type, 'foo')
        self.assertEqual(t.days, 0)
