from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.Facility.Exceptions.UnionTypeError import UnionTypeError


class UnionTypeField(OTLField):
    def __str__(self):
        return OTLField.__str__(self)

    attributen = None
    _uses_waarde_object = True

    @staticmethod
    def validate(value, attribuut):
        valueDict = vars(attribuut.field.waardeObject())
        for attr in valueDict.values():
            try:
                validate_result = attr.field.validate(value, attr)
                if validate_result:
                    return True
            except:
                continue
        raise UnionTypeError(f'Invalid value for {attribuut.naam}, check attr_type_info to see what kind of values are valid.')


