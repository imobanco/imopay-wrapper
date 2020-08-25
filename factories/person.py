from factory import Factory, LazyFunction
from factory.faker import Faker
from pycpfcnpj import gen

from imopay_wrapper.models.person import Person


class PersonFactory(Factory):
    class Meta:
        model = Person

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("safe_email")
    cpf = LazyFunction(gen.cpf)
    birthdate = Faker("date_of_birth", minimum_age=18)
    mobile_phone = Faker("cellphone_number", locale="pt-BR")
    phone = Faker("cellphone_number", locale="pt-BR")
