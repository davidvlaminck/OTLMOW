import decimal

from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class DecimalFloatField(PrimitiveField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version):
        super().__init__(float, naam, label, uri, definition, constraints, usagenote, deprecated_version)

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if (value is not None and (not isinstance(value, self.primitiveType) and not isinstance(value, int))) or (
                    value is not None and self.primitiveType in (int, float, decimal.Decimal) and isinstance(value, bool)):
                raise ValueError(f'expecting {self.primitiveType.__name__} in {self.naam}')
            elif value is not None:
                self.__dict__["waarde"] = float(value)
                return
        self.__dict__[name] = value