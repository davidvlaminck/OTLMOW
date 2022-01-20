from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.BaseClasses.KwantWrd import KwantWrd


class AttributeInfo:
    def info(self):
        return str(self)

    def attr_info(self, attribuut_naam=''):
        if '.' in attribuut_naam:
            attribuut = attribuut_naam.split('.')[0]
            rest = attribuut_naam.split('.', 1)[1]
            at = getattr(self, '_' + attribuut)
            print(at.field)
            if at.field._uses_waarde_object:
                return at.field.waardeObject().attr_info(rest)
            else:
                return at.attr_info(rest)
        else:
            if attribuut_naam == '':
                return str(self)
            at = getattr(self, '_' + attribuut_naam)
            return str(at)

    def attr_type_info(self, attribuut_naam):
        if '.' in attribuut_naam:
            attribuut = attribuut_naam.split('.')[0]
            rest = attribuut_naam.split('.', 1)[1]
            at = getattr(self, '_' + attribuut)
            if isinstance(at.field(), ComplexField):
                return at.field.waardeObject().attr_type_info(rest)
            else:
                return at.attr_type_info(rest)
        else:
            at = getattr(self, '_' + attribuut_naam)
            if isinstance(at.field(), KwantWrd):
                return str(at.field()) + str(at.field.eenheid)
            return str(at.field())