from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

cnpj = "foo"

response = client.company.retrieve(cnpj)

print(response.data)
