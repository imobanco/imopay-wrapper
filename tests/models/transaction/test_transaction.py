from unittest import TestCase

from imopay_wrapper.models.transaction import BaseTransaction


class BaseTransactionTestCase(TestCase):
    def test_(self):
        t = BaseTransaction.from_dict({})
        self.assertEqual(t.payer, None)
