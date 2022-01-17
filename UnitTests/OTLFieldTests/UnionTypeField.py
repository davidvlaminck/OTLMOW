from UnitTests.OTLFieldTests.OTLField import OTLField
from UnitTests.OTLFieldTests.UnionTypeError import UnionTypeError


class UnionTypeField(OTLField):
    attributen = None

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


