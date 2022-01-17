from abc import ABC
from OTLModel.BaseClasses.OTLField import OTLField


class ComplexField(OTLField, ABC):
    def __str__(self):
        return OTLField.__str__(self)

    _uses_waarde_object = True

    @staticmethod
    def validate(value, attribuut):
        raise ValueError(f'This is a complex datatype. Set the values through the attributes. Use .attr_type_info() for more info')

