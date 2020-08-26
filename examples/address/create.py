from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

a = {
    "owner": "algum id",
    "city": "Natal",
    "state": "RN",
    "zip_code": "99999999",
    "street": "Peterson Mills",
    "number": "9626",
    "neighborhood": "Crescent",
    "complement": "Senior condition research. City strategy such start",
}


response = client.address.create(a)
