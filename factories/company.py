from factory import Factory, LazyFunction
from factory.faker import Faker
from pycpfcnpj import gen

from imopay_wrapper.models.company import Company


class CompanyFactory(Factory):
    class Meta:
        model = Company

    cnpj = LazyFunction(gen.cnpj)
    commercial_name = Faker("bs")
    email = Faker("safe_email")
    opening_date = Faker("date_of_birth")
    social_name = Faker("company")
    website = Faker("url")
    phone = Faker("cellphone_number", locale="pt-BR")
