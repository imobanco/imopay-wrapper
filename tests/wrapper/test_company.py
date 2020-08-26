from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.models.company import Company


class CompanyWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().company

    def test_model(self):
        self.assertEqual(self.client.model, Company)

    def test_action(self):
        self.assertEqual(self.client.action, "companies")
