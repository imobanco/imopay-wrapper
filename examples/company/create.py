from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

data = {
    "email": "ilawson@example.net",
    "phone": "+55 74 99572 8196",
    "cnpj": "13415795551619",
    "opening_date": "1909-02-05",
    "social_name": "Hardy, Mann and Whitehead",
    "commercial_name": "maximize distributed deliverables",
    "website": "https://horton-black.info/",
}


response = client.company.create(data)

print(response.data)
