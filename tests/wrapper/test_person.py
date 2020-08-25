from ..utils import LocalImopayTestCase
from imopay_wrapper.wrapper.person import PersonWrapper
from factories.person import PersonFactory, Person


class PersonWrapperTestCase(LocalImopayTestCase):
    def test_create_update_retrieve(self):
        client = PersonWrapper()

        p = PersonFactory(first_name="original")

        response = client.create_person(p.to_dict())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("first_name"), "original")

        self.id = response.data.get("id")

        p = Person.from_dict({"first_name": "modificado"})

        response = client.update_person(self.id, p.to_dict())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("first_name"), "modificado")

        response = client.retrieve_person(self.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("first_name"), "modificado")
