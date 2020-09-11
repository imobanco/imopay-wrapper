from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

id = "foo"

response = client.company.retrieve(id)

print(response.data)
