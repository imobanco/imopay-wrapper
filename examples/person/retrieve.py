from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

imopay_id = "foo"

response = client.person.retrieve(imopay_id)

print(response.data)
