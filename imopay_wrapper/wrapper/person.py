from .base import BaseImopayWrapper
from ..models.person import Person


class PersonWrapper(BaseImopayWrapper):
    """
    Wrapper para os métodos de person
    """

    def create_person(self, data: dict):
        p = Person(**data)
        url = self._construct_url(action='persons')
        return self._post(url, p.to_dict())
