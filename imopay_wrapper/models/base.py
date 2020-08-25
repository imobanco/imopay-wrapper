from dataclasses import dataclass


@dataclass
class BaseImopayObj:
    @property
    def fields(self):
        return self.__class__.__dict__.get('__annotations__', {})

    def to_dict(self):
        data = {}
        for field_name, field_type in self.fields.items():
            data[field_name] = field_type(getattr(self, field_name))
        return data
