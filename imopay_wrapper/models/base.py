from dataclasses import dataclass
from typing import Union, Any
import inspect

from ..exceptions import FieldError, ValidationError


@dataclass
class BaseImopayObj:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __post_init__(self):
        self.__run_validators()
        self._init_nested_fields()

    def _init_nested_fields(self):
        pass

    @classmethod
    def get_fields(cls):
        # noinspection PyUnresolvedReferences
        return cls.__dataclass_fields__

    def to_dict(self):
        data = {}
        for field_name, field in self.get_fields().items():
            value = getattr(self, field_name)

            if self.is_empty_value(value):
                continue

            if isinstance(value, BaseImopayObj):
                data[field_name] = value.to_dict()
            else:
                data[field_name] = field.type(value)
        return data

    def __get_validation_methods(self):
        data = inspect.getmembers(self, predicate=inspect.ismethod)

        validation_methods = [item[1] for item in data if "_validate" in item[0]]

        return validation_methods

    def __run_validators(self):
        validation_methods = self.__get_validation_methods()

        errors = []

        for method in validation_methods:
            try:
                method()
            except FieldError as e:
                errors.append(e)

        if errors:
            raise ValidationError(self, errors)

    @classmethod
    def from_dict(cls, data: Union[dict, Any]):

        missing_fields = {
            field_name
            for field_name in cls.get_fields().keys()
            if field_name not in data.keys()
        }

        for missing_field in missing_fields:
            data[missing_field] = None

        return cls(**data)

    @staticmethod
    def is_empty_value(value):
        return value == "" or value is None
