# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class RVMS(EMObject):
    """Dynamische borden : rijwegvariabel geografisch route informatiepaneel (def. zie SB 270 hfdst 50)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RVMS'
    label = 'RVMS bord'

    def __init__(self):
        super().__init__()

        self._rvmsBuitenGebruik = EMAttribuut(field=BooleanField,
                                              naam='RVMS buiten gebruik',
                                              label='RVMS buiten gebruik',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RVMS.rvmsBuitenGebruik',
                                              definitie='Definitie nog toe te voegen voor eigenschap RVMS buiten gebruik')

        self._datumNieuweRvms = EMAttribuut(field=DateField,
                                            naam='datum nieuwe RVMS',
                                            label='datum nieuwe RVMS',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RVMS.datumNieuweRvms',
                                            definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe RVMS')

        self._drager = EMAttribuut(field=StringField,
                                   naam='drager',
                                   label='drager',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.drager',
                                   definitie='Definitie nog toe te voegen voor eigenschap drager')

        self._redenRvmsBuitenGebruik = EMAttribuut(field=StringField,
                                                   naam='reden RVMS buiten gebruik',
                                                   label='reden RVMS buiten gebruik',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#RVMS.redenRvmsBuitenGebruik',
                                                   definitie='Definitie nog toe te voegen voor eigenschap reden RVMS buiten gebruik')

    @property
    def rvmsBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap RVMS buiten gebruik"""
        return self._rvmsBuitenGebruik.waarde

    @rvmsBuitenGebruik.setter
    def rvmsBuitenGebruik(self, value):
        self._rvmsBuitenGebruik.set_waarde(value, owner=self)

    @property
    def datumNieuweRvms(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe RVMS"""
        return self._datumNieuweRvms.waarde

    @datumNieuweRvms.setter
    def datumNieuweRvms(self, value):
        self._datumNieuweRvms.set_waarde(value, owner=self)

    @property
    def drager(self):
        """Definitie nog toe te voegen voor eigenschap drager"""
        return self._drager.waarde

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)

    @property
    def redenRvmsBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden RVMS buiten gebruik"""
        return self._redenRvmsBuitenGebruik.waarde

    @redenRvmsBuitenGebruik.setter
    def redenRvmsBuitenGebruik(self, value):
        self._redenRvmsBuitenGebruik.set_waarde(value, owner=self)

