from .exceptions import FieldError


def _get_value_from_attr_or_value(obj, attr, value=None):
    """
    Método para extrair um valor de algum atributo do objeto.

    Caso seja passado um `value`, retorna o próprio value!

    Pode retornar None caso o atributo não exista!
    """
    if value is None:
        value = getattr(obj, attr, None)
    return value


def validate_obj_attr_type(obj, attr, types, value=None):
    """
    Método para validar que o valor de um atributo do objeto
    é de um determinado tipo.

    Note:
        pode ser passado uma tupla de tipos, o isinstance aceita isso!

    Caso o valor não seja do tipo, lança o erro!
    """
    value = _get_value_from_attr_or_value(obj, attr, value=value)

    if not isinstance(value, types):
        raise FieldError(attr, f"{value} não é do tipo {types}")


def validate_obj_attr_in_collection(obj, attr, collection, value=None):
    """
    Método para validar que o valor de um atributo do objeto
    está na coleção de possíveis valores.

    Caso o valor não esteja na coleção, lança o erro!
    """
    value = _get_value_from_attr_or_value(obj, attr, value=value)

    if value not in collection:
        raise FieldError(attr, f"{value} não está na coleção {collection}")
