from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from factories.person import Person


class PersonWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().person

    def test_model(self):
        self.assertEqual(self.client.model, Person)

    def test_action(self):
        self.assertEqual(self.client.action, "persons")
