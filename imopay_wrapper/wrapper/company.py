from .base import BaseImopayWrapper
from ..models.company import Company


class CompanyWrapper(BaseImopayWrapper):
    """
    Wrapper para os métodos de company
    """

    @property
    def model(self):
        return Company

    @property
    def action(self):
        return "companies"

    def search(self, value):
        data = {
            "cnpj": value
        }
        url = self._construct_url(action=self.action, subaction='search')
        return self._post(url, data)
