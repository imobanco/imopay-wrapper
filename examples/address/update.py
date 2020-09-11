from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

id = "foo"

data = {
    "owner": "bar",
    "city": "Natal",
    "uf": "RN",
    "zip_code": "59100000",
    "street": "Rua Qualquer",
    "number": 11111,
    "neighborhood": "Tirol",
    "complement": None,
}

response = client.address.update(id, data)

print(response.data)
