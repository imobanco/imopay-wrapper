from ..utils import LocalImopayTestCase
from imopay_wrapper.wrapper.person import PersonWrapper
from factories.person import PersonFactory, Person


class PersonWrapperTestCase(LocalImopayTestCase):
    def test_create(self):
        client = PersonWrapper()

        p = PersonFactory()

        response = client.create_person(p.to_dict())

        self.assertEqual(response.status_code, 201)

    def test_update_put(self):
        client = PersonWrapper()

        p = PersonFactory(first_name='original')

        response = client.create_person(p.to_dict())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('first_name'), 'original')

        id = response.data.get('id')

        p = Person.from_dict({'first_name': 'modificado'})

        response = client.update_person(id, p.to_dict())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('first_name'), 'modificado')
