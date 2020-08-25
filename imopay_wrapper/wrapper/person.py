from .base import BaseImopayWrapper
from ..models.person import Person


class PersonWrapper(BaseImopayWrapper):
    """
    Wrapper para os métodos de person
    """

    def create_person(self, data: dict):
        p = Person.from_dict(data)
        url = self._construct_url(action="persons")
        return self._post(url, p.to_dict())

    def update_person(self, identifier: str, data: dict):
        p = Person.from_dict(data)
        url = self._construct_url(action="persons", identifier=identifier)
        return self._patch(url, p.to_dict())

    def retrieve_person(self, identifier: str):
        url = self._construct_url(action="persons", identifier=identifier)
        return self._get(url)
