from factory import Factory
from factory.faker import Faker

from imopay_wrapper.models.address import Address


class AddressFactory(Factory):
    class Meta:
        model = Address

    owner = "algum id"
    city = "Natal"
    state = "RN"

    zip_code = "99999999"
    street = Faker("street_name")
    number = Faker("building_number")

    neighborhood = Faker("street_suffix")

    complement = Faker("text", max_nb_chars=100)
