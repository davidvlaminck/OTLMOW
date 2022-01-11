import copy
from abc import ABC, abstractmethod
from datetime import datetime

from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


class AttributeSetterFactory:  # TODO write tests
    @classmethod
    def CreateSetter(cls, instance, attr_naam=None):
        if attr_naam is not None:
            try:
                attribute = getattr(instance, attr_naam)
            except AttributeError as ex:
                if attr_naam == "bron" or attr_naam == "doel":
                    return None  # TODO decide whether or not to implement bron and doel attributes of relatie
                raise NotImplementedError(str(ex))
        else:
            attribute = instance

        if isinstance(attribute, KeuzelijstField):
            return KeuzelijstFieldSetter(attribute)
        elif isinstance(attribute, ComplexField):
            return ComplexFieldSetter(attribute)
        elif isinstance(attribute, DateField):
            return DateFieldSetter(attribute)
        elif isinstance(attribute, KardinaliteitField):
            return KardinaliteitFieldSetter(attribute)
        else:
            return PrimitiveFieldSetter(attribute)


class AbstractAttributeSetter(ABC):
    @abstractmethod
    def set_attribute(self, value):
        pass


class KeuzelijstFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.set_value_by_invulwaarde(value.split('/')[-1])


class PrimitiveFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = value


class KardinaliteitFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attributeComplex(self, value):  # TODO write test
        lijstValues = []
        for valueDict in value:
            attributeInstance = copy.deepcopy(self.attribute.fieldToMultiply)
            for k, v in valueDict.items():
                attr_naam = k.split('.')[-1]
                attribute_setter = AttributeSetterFactory.CreateSetter(self.attribute, attr_naam)
                attribute_setter.set_attribute(v)
            lijstValues.append(attributeInstance)
        self.attribute.waarde = lijstValues

    def set_attribute(self, valueList):  # TODO write test
        lijstValues = []
        for value_iter in valueList:
            attributeInstance = copy.deepcopy(self.attribute.fieldToMultiply)
            if isinstance(value_iter, str):
                attr_naam = 'fieldToMultiply'
                attribute_setter = AttributeSetterFactory.CreateSetter(attributeInstance)
                attribute_setter.set_attribute(value_iter)
            elif isinstance(value_iter, dict):
                for k, v in value_iter.items():
                    attr_naam = k.split('.')[-1]
                    attribute_setter = AttributeSetterFactory.CreateSetter(self.attribute, attr_naam)
                    attribute_setter.set_attribute(v)
            else:
                raise NotImplementedError
            lijstValues.append(attributeInstance)
        self.attribute.waarde = lijstValues


class ComplexFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        for k, v in value.items():
            attr_naam = k.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(self.attribute, attr_naam)
            attribute_setter.set_attribute(v)


class DateFieldSetter(AbstractAttributeSetter):
    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, value):  # TODO write test
        self.attribute.waarde = datetime.strptime(value, '%Y-%m-%d')