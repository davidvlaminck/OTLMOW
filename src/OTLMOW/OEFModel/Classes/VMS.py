# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class VMS(EMObject):
    """Dynamische borden : Variabel tekstueel bord (definitie zie SB 270, hfdst 50)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VMS'
    label = 'VMS bord'

    def __init__(self):
        super().__init__()

        self._vmsBuitenGebruik = EMAttribuut(field=BooleanField,
                                             naam='VMS buiten gebruik',
                                             label='VMS buiten gebruik',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VMS.vmsBuitenGebruik',
                                             definitie='Definitie nog toe te voegen voor eigenschap VMS buiten gebruik')

        self._datumNieuweVms = EMAttribuut(field=DateField,
                                           naam='datum nieuwe VMS',
                                           label='datum nieuwe VMS',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VMS.datumNieuweVms',
                                           definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe VMS')

        self._drager = EMAttribuut(field=StringField,
                                   naam='drager',
                                   label='drager',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.drager',
                                   definitie='Definitie nog toe te voegen voor eigenschap drager')

        self._redenVmsBuitenGebruik = EMAttribuut(field=StringField,
                                                  naam='reden VMS buiten gebruik',
                                                  label='reden VMS buiten gebruik',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#VMS.redenVmsBuitenGebruik',
                                                  definitie='Definitie nog toe te voegen voor eigenschap reden VMS buiten gebruik')

    @property
    def vmsBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap VMS buiten gebruik"""
        return self._vmsBuitenGebruik.waarde

    @vmsBuitenGebruik.setter
    def vmsBuitenGebruik(self, value):
        self._vmsBuitenGebruik.set_waarde(value, owner=self)

    @property
    def datumNieuweVms(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe VMS"""
        return self._datumNieuweVms.waarde

    @datumNieuweVms.setter
    def datumNieuweVms(self, value):
        self._datumNieuweVms.set_waarde(value, owner=self)

    @property
    def drager(self):
        """Definitie nog toe te voegen voor eigenschap drager"""
        return self._drager.waarde

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)

    @property
    def redenVmsBuitenGebruik(self):
        """Definitie nog toe te voegen voor eigenschap reden VMS buiten gebruik"""
        return self._redenVmsBuitenGebruik.waarde

    @redenVmsBuitenGebruik.setter
    def redenVmsBuitenGebruik(self, value):
        self._redenVmsBuitenGebruik.set_waarde(value, owner=self)

