from imopay_wrapper import ImopayWrapper


client = ImopayWrapper()

data = {
    "owner": "ID_DO_SELLER",
    "bank": '001',
    "type": "corrente",
    "number": "123123",
    "routing": "45678"
}

response = client.bank_account.create(data)

print(response.data)
