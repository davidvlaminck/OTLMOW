import copy
from abc import ABC, abstractmethod
from datetime import datetime

from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


class AttributeSetterFactory:  # TODO write tests
    @classmethod
    def CreateSetter(cls, instance, attr_naam=None):
        if attr_naam is not None:
            try:
                attribute = getattr(instance, '_' + attr_naam)
            except AttributeError as ex:
                if attr_naam == "bron" or attr_naam == "doel":
                    return None  # TODO decide whether or not to implement bron and doel attributes of relatie
                raise NotImplementedError(str(ex))
        else:
            attribute = instance

        if attribute.field.waardeObject is not None:
            return ComplexFieldSetter(attribute)
        return PrimitiveFieldSetter(attribute)

class AbstractAttributeSetter(ABC):
    @abstractmethod
    def set_attribute(self, value):
        pass


class KeuzelijstFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = value


class PrimitiveFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = value


class ComplexFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute
        if self.attribute.naam == 'externeReferentie':
            pass

    def set_attribute(self, value):
        if type(value) is list:
            valueList = []
            for item in value:
                waardeObject = self.attribute.field.waardeObject()
                self.set_complex_attribute(value=item, attribuut=waardeObject)
                valueList.append(waardeObject)
            self.attribute.waarde = valueList
        else:
            self.set_complex_attribute(value)

    def set_complex_attribute(self, value, attribuut=None):
        for k, v in value.items():
            attr_naam = k.split('.')[-1]
            if attribuut is None:
                attribute_setter = AttributeSetterFactory.CreateSetter(self.attribute.waarde, attr_naam)
            else:
                attribute_setter = AttributeSetterFactory.CreateSetter(attribuut, attr_naam)
            attribute_setter.set_attribute(v)


class DateFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = datetime.strptime(value, '%Y-%m-%d')