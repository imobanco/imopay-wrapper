from .exceptions import FieldError


def _get_value_from_attr_or_value(obj, attr, value=None):
    if value is None:
        value = getattr(obj, attr)
    return value


def validate_obj_attr_type(obj, attr, types, value=None):
    value = _get_value_from_attr_or_value(obj, attr, value=value)

    if not isinstance(value, types):
        raise FieldError(attr, f"{value} não é do tipo {types}")


def validate_obj_attr_in_collection(obj, attr, collection, value=None):
    value = _get_value_from_attr_or_value(obj, attr, value=value)

    if value not in collection:
        raise FieldError(attr, f"{value} não está na coleção {collection}")
