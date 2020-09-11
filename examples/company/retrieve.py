from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

imopay_id = "foo"

response = client.company.retrieve(imopay_id)

print(response.data)
