from OTLMOW.OTLModel.Datatypes import ComplexField
from OTLMOW.OTLModel.BaseClasses.KwantWrd import KwantWrd


class AttributeInfo:
    def __init__(self):
        self._parent = None

    def info(self):
        return str(self)

    def info_attr(self, attribuut_naam=''):
        if '.' in attribuut_naam:
            attribuut = attribuut_naam.split('.')[0]
            rest = attribuut_naam.split('.', 1)[1]
            at = getattr(self, '_' + attribuut)
            if at.field._uses_waarde_object:
                return at.field.waardeObject().info_attr(rest)
            else:
                return at.info_attr(rest)
        else:
            if attribuut_naam == '':
                s = f'Attribute information about {self.__class__.__name__} {self.__hash__()}:\n'
                for k, v in sorted(vars(self).items()):
                    if v is not None and k not in ['_parent', '_geometry', '_geometry_types']:
                        s += f'{k[1:]} (type: {v.field.naam})\n'
                return s
            at = getattr(self, '_' + attribuut_naam)
            return str(at)

    def info_attr_type(self, attribuut_naam):
        if '.' in attribuut_naam:
            attribuut = attribuut_naam.split('.')[0]
            rest = attribuut_naam.split('.', 1)[1]
            at = getattr(self, '_' + attribuut)
            if isinstance(at.field(), ComplexField):
                return at.field.waardeObject().info_attr_type(rest)
            else:
                return at.info_attr_type(rest)
        else:
            at = getattr(self, '_' + attribuut_naam)

            if isinstance(at.field(), KwantWrd):
                return str(at.field()) + str(at.field.eenheid)
            s = str(at.field())
            if at.field.waardeObject is not None:
                s += '\n\n' + at.waarde.info_attr('')
            return s
