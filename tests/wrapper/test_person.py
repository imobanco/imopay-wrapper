from ..utils import LocalImopayTestCase
from imopay_wrapper import ImopayWrapper
from factories.person import PersonFactory, Person


class PersonWrapperTestCase(LocalImopayTestCase):
    def test_create_update_retrieve(self):
        client = ImopayWrapper()
        person_client = client.person

        p = PersonFactory(first_name="original")

        response = person_client.create(p.to_dict())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("first_name"), "original")

        id = response.data.get("id")

        p = Person.from_dict({"first_name": "modificado"})

        response = person_client.update(id, p.to_dict())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("first_name"), "modificado")

        response = person_client.retrieve(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("first_name"), "modificado")
