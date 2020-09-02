from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

document = "cpf/cnpj qualquer"

response = client.address.get_by_document(document)

print(response)
