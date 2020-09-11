import logging

from imopay_wrapper import ImopayWrapper


logger = logging.getLogger()


client = ImopayWrapper()

data = {
    "url": "http://494830363d1d.ngrok.io",
    "event": "t",
    "description": "webhook de teste"
}

response = client.webhook.create(data)

print(response.data)
