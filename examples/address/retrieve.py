from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

id = "foo"

response = client.address.retrieve(id)

print(response)
