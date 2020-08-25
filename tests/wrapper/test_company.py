from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from factories.company import CompanyFactory, Company


class CompanyWrapperTestCase(LocalImopayTestCase):
    def test_create(self):
        client = ImopayWrapper()
        company_client = client.company

        c = CompanyFactory(social_name='original')

        response = company_client.create(c.to_dict())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("social_name"), "original")

        id = response.data.get("id")

        c = Company.from_dict({"social_name": "modificado"})

        response = company_client.update(id, c.to_dict())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("social_name"), "modificado")

        response = company_client.retrieve(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("social_name"), "modificado")
