import decimal

from ModelGenerator.BaseClasses.IntField import IntField
from ModelGenerator.BaseClasses.PrimitiveField import PrimitiveField


class NonNegIntField(IntField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly=False, readonlyValue=None):
        super().__init__(naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)

    def __setattr__(self, name, value):
        if type(self) == NonNegIntField:
            if name == "waarde" and self.readonly and value is not None:
                raise AttributeError(f"can't set the value of a readonly attribute")
            if name == "waarde":
                if (value is not None and not isinstance(value, self.primitiveType)) or (
                        value is not None and self.primitiveType in (int, float, decimal.Decimal) and isinstance(value, bool)):
                    raise ValueError(f'expecting {self.primitiveType.__name__} in {self.naam}')
                if value is not None and value < 0:
                    raise ValueError(f'expecting non negative integer in {self.naam}')
            self.__dict__[name] = value
