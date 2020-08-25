from unittest import TestCase

from imopay_wrapper.wrapper.person import PersonWrapper
from factories.person import PersonFactory


class PersonWrapperTestCase(TestCase):
    def test_create(self):
        client = PersonWrapper()

        p = PersonFactory()

        client.create_person(p.to_dict())
