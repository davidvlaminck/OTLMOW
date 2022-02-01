# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class SeinbrugDVM(EMObject):
    """Mechanische contructie DVM installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SeinbrugDVM'
    label = 'Seinbrug DVM'

    def __init__(self):
        super().__init__()

        self._ralKleur = EMAttribuut(field=StringField,
                                     naam='RAL kleur',
                                     label='RAL kleur',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.ralKleur',
                                     definitie='Definitie nog toe te voegen voor eigenschap RAL kleur')

        self._borgingLeuningenAangebracht = EMAttribuut(field=StringField,
                                                        naam='borging leuningen aangebracht',
                                                        label='borging leuningen aangebracht',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.borgingLeuningenAangebracht',
                                                        definitie='Definitie nog toe te voegen voor eigenschap toestand boutverbinding')

        self._datumNieuweBescherming = EMAttribuut(field=DateField,
                                                   naam='datum nieuwe bescherming',
                                                   label='datum nieuwe bescherming',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.datumNieuweBescherming',
                                                   definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe bescherming')

        self._datumNieuweSeinbrugDvm = EMAttribuut(field=DateField,
                                                   naam='datum nieuwe seinbrug DVM',
                                                   label='datum nieuwe seinbrug DVM',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.datumNieuweSeinbrugDvm',
                                                   definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe seinbrug DVM')

        self._lengteOverspanning = EMAttribuut(field=FloatOrDecimalField,
                                               naam='lengte overspanning',
                                               label='lengte overspanning',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.lengteOverspanning',
                                               definitie='Definitie nog toe te voegen voor eigenschap lengte overspanning')

        self._minimumVrijeHoogte = EMAttribuut(field=FloatOrDecimalField,
                                               naam='minimum vrije hoogte',
                                               label='minimum vrije hoogte',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.minimumVrijeHoogte',
                                               definitie='Definitie nog toe te voegen voor eigenschap minimum vrije hoogte')

        self._redenSeinbrugDvmVerwijderd = EMAttribuut(field=StringField,
                                                       naam='reden seinbrug DVM verwijderd',
                                                       label='reden seinbrug DVM verwijderd',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.redenSeinbrugDvmVerwijderd',
                                                       definitie='Definitie nog toe te voegen voor eigenschap reden seinbrug DVM verwijderd')

        self._seinbrugDvmVerwijderd = EMAttribuut(field=BooleanField,
                                                  naam='seinbrug DVM verwijderd',
                                                  label='seinbrug DVM verwijderd',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.seinbrugDvmVerwijderd',
                                                  definitie='Definitie nog toe te voegen voor eigenschap seinbrug DVM verwijderd')

        self._typeESeinbrug = EMAttribuut(field=StringField,
                                          naam='type E-seinbrug',
                                          label='type E-seinbrug',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.typeESeinbrug',
                                          definitie='Definitie nog toe te voegen voor eigenschap type E-seinbrug')

        self._typeBescherming = EMAttribuut(field=StringField,
                                            naam='type bescherming',
                                            label='type bescherming',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.typeBescherming',
                                            definitie='Definitie nog toe te voegen voor eigenschap type bescherming')

        self._typeSeinbrug = EMAttribuut(field=StringField,
                                         naam='type seinbrug',
                                         label='type seinbrug',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.typeSeinbrug',
                                         definitie='Definitie nog toe te voegen voor eigenschap type seinbrug')

    @property
    def ralKleur(self):
        """Definitie nog toe te voegen voor eigenschap RAL kleur"""
        return self._ralKleur.waarde

    @ralKleur.setter
    def ralKleur(self, value):
        self._ralKleur.set_waarde(value, owner=self)

    @property
    def borgingLeuningenAangebracht(self):
        """Definitie nog toe te voegen voor eigenschap toestand boutverbinding"""
        return self._borgingLeuningenAangebracht.waarde

    @borgingLeuningenAangebracht.setter
    def borgingLeuningenAangebracht(self, value):
        self._borgingLeuningenAangebracht.set_waarde(value, owner=self)

    @property
    def datumNieuweBescherming(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe bescherming"""
        return self._datumNieuweBescherming.waarde

    @datumNieuweBescherming.setter
    def datumNieuweBescherming(self, value):
        self._datumNieuweBescherming.set_waarde(value, owner=self)

    @property
    def datumNieuweSeinbrugDvm(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe seinbrug DVM"""
        return self._datumNieuweSeinbrugDvm.waarde

    @datumNieuweSeinbrugDvm.setter
    def datumNieuweSeinbrugDvm(self, value):
        self._datumNieuweSeinbrugDvm.set_waarde(value, owner=self)

    @property
    def lengteOverspanning(self):
        """Definitie nog toe te voegen voor eigenschap lengte overspanning"""
        return self._lengteOverspanning.waarde

    @lengteOverspanning.setter
    def lengteOverspanning(self, value):
        self._lengteOverspanning.set_waarde(value, owner=self)

    @property
    def minimumVrijeHoogte(self):
        """Definitie nog toe te voegen voor eigenschap minimum vrije hoogte"""
        return self._minimumVrijeHoogte.waarde

    @minimumVrijeHoogte.setter
    def minimumVrijeHoogte(self, value):
        self._minimumVrijeHoogte.set_waarde(value, owner=self)

    @property
    def redenSeinbrugDvmVerwijderd(self):
        """Definitie nog toe te voegen voor eigenschap reden seinbrug DVM verwijderd"""
        return self._redenSeinbrugDvmVerwijderd.waarde

    @redenSeinbrugDvmVerwijderd.setter
    def redenSeinbrugDvmVerwijderd(self, value):
        self._redenSeinbrugDvmVerwijderd.set_waarde(value, owner=self)

    @property
    def seinbrugDvmVerwijderd(self):
        """Definitie nog toe te voegen voor eigenschap seinbrug DVM verwijderd"""
        return self._seinbrugDvmVerwijderd.waarde

    @seinbrugDvmVerwijderd.setter
    def seinbrugDvmVerwijderd(self, value):
        self._seinbrugDvmVerwijderd.set_waarde(value, owner=self)

    @property
    def typeESeinbrug(self):
        """Definitie nog toe te voegen voor eigenschap type E-seinbrug"""
        return self._typeESeinbrug.waarde

    @typeESeinbrug.setter
    def typeESeinbrug(self, value):
        self._typeESeinbrug.set_waarde(value, owner=self)

    @property
    def typeBescherming(self):
        """Definitie nog toe te voegen voor eigenschap type bescherming"""
        return self._typeBescherming.waarde

    @typeBescherming.setter
    def typeBescherming(self, value):
        self._typeBescherming.set_waarde(value, owner=self)

    @property
    def typeSeinbrug(self):
        """Definitie nog toe te voegen voor eigenschap type seinbrug"""
        return self._typeSeinbrug.waarde

    @typeSeinbrug.setter
    def typeSeinbrug(self, value):
        self._typeSeinbrug.set_waarde(value, owner=self)

