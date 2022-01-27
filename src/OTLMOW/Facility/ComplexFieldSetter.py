from OTLMOW.Facility.AbstractAttributeSetter import AbstractAttributeSetter
from OTLMOW.Facility.AttributeSetterFactory import AttributeSetterFactory


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
            if self.attribute.field._uses_waarde_object:
                self.set_complex_attribute(value)
            else:
                self.attribute.waarde = value

    def set_complex_attribute(self, value, attribuut=None):
        for k, v in value.items():
            attr_naam = k.split('.')[-1]
            if attribuut is None:
                attribute_setter = AttributeSetterFactory.CreateSetter(self.attribute.waarde, attr_naam)
            else:
                attribute_setter = AttributeSetterFactory.CreateSetter(attribuut, attr_naam)
            attribute_setter.set_attribute(v)