import numbers

from ..external import six

from .._internal_utils import arg_handler

from . import _VertaDataType


class NumericValue(_VertaDataType):
    """
    Representation of a number.

    Parameters
    ----------
    value : float
        Number.
    unit : str
        Unit of measurement.

    Examples
    --------
    .. code-block:: python

        from verta.data_types import NumericValue
        data = NumericValue(4, unit="lbs")
        run.log_attribute("weight", data)

    """

    _TYPE_NAME = "numericValue"
    _VERSION = "v1"

    @arg_handler.args_to_builtin(ignore_self=True)
    def __init__(self, value, unit=None):
        if not isinstance(value, numbers.Real):
            raise TypeError("`value` must be a number, not {}".format(type(value)))
        if unit and not isinstance(unit, six.string_types):
            raise TypeError("`unit` must be a string, not {}".format(type(unit)))

        self._value = value
        self._unit = unit

    def _as_dict(self):
        data = {"value": self._value}
        if self._unit:
            data["unit"] = self._unit
        return self._as_dict_inner(data)

    @classmethod
    def _from_dict_inner(cls, d):
        data = d[cls._TYPE_NAME]
        return cls(
            value=data["value"],
            unit=data.get("unit"),
        )