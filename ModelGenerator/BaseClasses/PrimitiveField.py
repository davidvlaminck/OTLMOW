import decimal
from abc import ABC

from ModelGenerator.BaseClasses.OTLField import OTLField


class PrimitiveField(OTLField, ABC):
    def __init__(self, primitiveType: type, naam, label, uri, definition, constraints, usagenote, deprecated_version,
                 readonly=False, readonlyValue=None):
        super().__init__(naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)
        self.primitiveType = primitiveType

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if (value is not None and not isinstance(value, self.primitiveType)) or (
                    value is not None and self.primitiveType in (int, float, decimal.Decimal) and isinstance(value, bool)):
                raise ValueError(f'expecting {self.primitiveType.__name__} in {self.naam}')
        self.__dict__[name] = value
