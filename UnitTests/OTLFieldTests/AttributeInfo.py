from UnitTests.OTLFieldTests.ComplexField import ComplexField


class AttributeInfo:
    def attr_info(self, attribuut_naam):
        if '.' in attribuut_naam:
            attribuut = attribuut_naam.split('.')[0]
            rest = attribuut_naam.split('.', 1)[1]
            at = getattr(self, '_' + attribuut)
            if isinstance(at.field, ComplexField):
                return at.waarde.attr_info(rest)
            else:
                return at.attr_info(rest)
        else:
            at = getattr(self, '_' + attribuut_naam)
            return str(at)

    def attr_type_info(self, attribuut_naam):
        if '.' in attribuut_naam:
            attribuut = attribuut_naam.split('.')[0]
            rest = attribuut_naam.split('.', 1)[1]
            at = getattr(self, '_' + attribuut)
            if isinstance(at.field(), ComplexField):
                return at.waarde.attr_type_info(rest)
            else:
                return at.attr_type_info(rest)
        else:
            at = getattr(self, '_' + attribuut_naam)
            return str(at.field)