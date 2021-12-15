import math

from OTLModel.Datatypes.OTLField import OTLField
from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class KardinaliteitField(OTLField):
    def __init__(self, minKardinaliteit: str, maxKardinaliteit: str, fieldToMultiply: OTLField):
        OTLField.__init__(self, naam=fieldToMultiply.naam, label=fieldToMultiply.label, uri=fieldToMultiply.uri,
                          definition=fieldToMultiply.definition, constraints=fieldToMultiply.constraints,
                          usagenote=fieldToMultiply.usagenote, deprecated_version=fieldToMultiply.deprecated_version)
        self.fieldToMultiply = fieldToMultiply
        self.minKardinaliteit = int(minKardinaliteit)
        if maxKardinaliteit == '*':
            self.maxKardinaliteit = math.inf
        else:
            self.maxKardinaliteit = int(maxKardinaliteit)
        self.__dict__["waarde"] = []

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if value is None:
                self.__dict__["waarde"] = value
                return
            elif not isinstance(value, list):
                raise ValueError(f'expecting list in {self.naam}.{name}')
            elif len(value) < self.minKardinaliteit:
                raise ValueError(f'expecting at least {self.minKardinaliteit} element(s) in {self.naam}.{name}')
            elif len(value) > self.maxKardinaliteit:
                raise ValueError(f'expecting at most {self.maxKardinaliteit} element(s) in {self.naam}.{name}')
            bad_type = self.check_types_in_list(value)
            if bad_type:
                raise ValueError(f'element of bad type in {self.naam}.{name}')
        self.__dict__[name] = value

    def check_types_in_list(self, valueList) -> bool:
        bad_type = False
        for el in valueList:
            if isinstance(self.fieldToMultiply, PrimitiveField):
                if not (isinstance(el, self.fieldToMultiply.primitiveType)):
                    bad_type = True
                    return bad_type
            else:
                if not (isinstance(el, self.fieldToMultiply.__class__)):
                    bad_type = True
                    return bad_type
        return bad_type
