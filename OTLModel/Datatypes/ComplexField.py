from abc import ABC
from OTLModel.BaseClasses.OTLField import OTLField


class ComplexField(OTLField, ABC):
    def __str__(self):
        return OTLField.__str__(self)

    _uses_waarde_object = True

    @staticmethod
    def validate(value, attribuut):
        if not isinstance(value, attribuut.field.waardeObject):
            raise ValueError(f'This is a complex datatype. Set the values through the attributes. Use .attr_type_info() for more info')
        validation = True
        for tuple in vars(value).items():
            waarde = tuple[0]
            attr = tuple[1]
            if not attr.field.validate(waarde, attr):
                validation = False
        return validation

