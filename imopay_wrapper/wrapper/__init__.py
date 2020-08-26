from .company import CompanyWrapper
from .person import PersonWrapper


class ImopayWrapper:
    def __init__(self):
        self.company = CompanyWrapper()
        self.person = PersonWrapper()
