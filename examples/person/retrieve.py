from imopay_wrapper import ImopayWrapper

client = ImopayWrapper()

id = 'foo'

response = client.person.retrieve(id)
