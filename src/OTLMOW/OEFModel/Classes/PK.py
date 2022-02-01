# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class PK(EMObject):
    """Dynamische borden : Pijl-kruis bord (def. SB 270 hfdst 50)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#PK'
    label = 'Pijl-kruis bord'

    def __init__(self):
        super().__init__()

        self._pkBuitenGebruik = EMAttribuut(field=BooleanField,
                                            naam='PK buiten gebruik',
                                            label='PK buiten gebruik',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#PK.pkBuitenGebruik',
                                            definitie='Definitie nog toe te voegen voor eigenschap PK buiten gebruik')

        self._datumNieuwePk = EMAttribuut(field=DateField,
                                          naam='datum nieuwe PK',
                                          label='datum nieuwe PK',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#PK.datumNieuwePk',
                                          definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe PK')

        self._drager = EMAttribuut(field=StringField,
                                   naam='drager',
                                   label='drager',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.drager',
                                   definitie='Definitie nog toe te voegen voor eigenschap drager')

        self._redenPkBuitenGebruik = EMAttribuut(field=StringField,
                                                 naam='reden PK buiten gebruik',
                                                 label='reden PK buiten gebruik',
                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#PK.redenPkBuitenGebruik',
                                                 definitie='Definitie nog toe te voegen voor eigenschap reden PK buiten gebruik')

    @property
    def pkBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap PK buiten gebruik"""
        return self._pkBuitenGebruik.waarde

    @pkBuitenGebruik.setter
    def pkBuitenGebruik(self, value):
        self._pkBuitenGebruik.set_waarde(value, owner=self)

    @property
    def datumNieuwePk(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe PK"""
        return self._datumNieuwePk.waarde

    @datumNieuwePk.setter
    def datumNieuwePk(self, value):
        self._datumNieuwePk.set_waarde(value, owner=self)

    @property
    def drager(self):
        """Definitie nog toe te voegen voor eigenschap drager"""
        return self._drager.waarde

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)

    @property
    def redenPkBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden PK buiten gebruik"""
        return self._redenPkBuitenGebruik.waarde

    @redenPkBuitenGebruik.setter
    def redenPkBuitenGebruik(self, value):
        self._redenPkBuitenGebruik.set_waarde(value, owner=self)

