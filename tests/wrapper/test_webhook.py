from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from imopay_wrapper.models.webhook import Webhook


class WebhookWrapperTestCase(LocalImopayTestCase):
    def setUp(self):
        self.client = ImopayWrapper().webhook

    def test_model(self):
        self.assertEqual(self.client.model, Webhook)

    def test_action(self):
        self.assertEqual(self.client.action, "webhooks")
