import copy
import math

from OTLModel.Datatypes.OTLField import OTLField
from OTLModel.Datatypes.PrimitiveField import PrimitiveField


class KardinaliteitField(OTLField):
    def __init__(self, minKardinaliteit: str, maxKardinaliteit: str, fieldToMultiply: OTLField):
        OTLField.__init__(self, naam=fieldToMultiply.naam, label=fieldToMultiply.label, objectUri=fieldToMultiply.objectUri,
                          definition=fieldToMultiply.definition, constraints=fieldToMultiply.constraints,
                          usagenote=fieldToMultiply.usagenote, deprecated_version=fieldToMultiply.deprecated_version)
        self.fieldToMultiply = fieldToMultiply
        self.minKardinaliteit = int(minKardinaliteit)
        if maxKardinaliteit == '*':
            self.maxKardinaliteit = math.inf
        else:
            self.maxKardinaliteit = int(maxKardinaliteit)
        self.__dict__["waarde"] = []

    def set_waarde_by_index(self, value, index):
        if self.waarde is None:
            self.waarde = []
        instanceField = copy.deepcopy(self.fieldToMultiply)
        instanceField.waarde = value
        while index >= len(self.waarde):
            self.waarde.append(None)
        self.waarde[index] = instanceField

    def waarde_index(self, index):
        return self.waarde[index].waarde

    def volgende_waarde(self):
        for val in self.waarde:
            yield val.waarde

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if value is None or value == []:
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
            valueList = []
            for el in value:
                if isinstance(el, type(self.fieldToMultiply)):
                    valueList.append(el)
                else:
                    instanceField = copy.deepcopy(self.fieldToMultiply)
                    instanceField.waarde = el
                    valueList.append(instanceField)
            self.__dict__[name] = valueList
            return
        self.__dict__[name] = value

    def check_types_in_list(self, valueList) -> bool:
        bad_type = False
        for el in valueList:
            if isinstance(self.fieldToMultiply, PrimitiveField):
                try:
                    if not (isinstance(el.waarde, self.fieldToMultiply.primitiveType)):
                        return True
                except AttributeError:
                    if not (isinstance(el, self.fieldToMultiply.primitiveType)):
                        return True
            else:
                if not (isinstance(el, self.fieldToMultiply.__class__)):
                    return True
        return bad_type

    def default(self):
        lijstValues = []
        for element in self.waarde:
            lijstValues.append(element.default())
        return lijstValues

