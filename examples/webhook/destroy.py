import logging

from imopay_wrapper import ImopayWrapper


logger = logging.getLogger()


client = ImopayWrapper()

imopay_id = 'dea9064b-f5ec-40c7-8e1b-15ddeff5e3b5'

response = client.webhook.destroy(imopay_id)

print(response.data)
