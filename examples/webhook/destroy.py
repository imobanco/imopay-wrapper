from imopay_wrapper import ImopayWrapper


client = ImopayWrapper()

imopay_imopay_id = "foo"

response = client.webhook.destroy(imopay_imopay_id)

print(response.data)
