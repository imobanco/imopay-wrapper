from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

cpf = "foo"

response = client.person.retrieve(cpf)

print(response.data)
