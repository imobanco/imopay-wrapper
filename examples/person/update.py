from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

imopay_id = "foo"

data = {
    "email": "tyler13@example.net",
    "phone": "+55 (019) 92498 1907",
    "first_name": "William",
    "last_name": "Clark",
    "cpf": "63304280693",
    "birthdate": "1947-04-11",
    "mobile_phone": "+55 60 97852 2366",
}

response = client.person.update(imopay_id, data)

print(response.data)
