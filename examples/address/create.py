from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

data = {
    "owner": "algum id",
    "city": "Natal",
    "uf": "RN",
    "zip_code": "99999999",
    "street": "Peterson Mills",
    "number": "9626",
    "neighborhood": "Crescent",
    "complement": "Senior condition research. City strategy such start",
}


response = client.address.create(data)

print(response.data)
