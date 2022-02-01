# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class WV(EMObject):
    """Wegverlichtingsinstallatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#WV'
    label = 'Wegverlichtingsinstallatie'

    def __init__(self):
        super().__init__()

        self._gedimdTussen = EMAttribuut(field=StringField,
                                         naam='gedimd tussen',
                                         label='gedimd tussen',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#WV.gedimdTussen',
                                         definitie='Definitie nog toe te voegen voor eigenschap gedimd tussen')

        self._gedoofdTussen = EMAttribuut(field=StringField,
                                          naam='gedoofd tussen',
                                          label='gedoofd tussen',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#WV.gedoofdTussen',
                                          definitie='Definitie nog toe te voegen voor eigenschap gedoofd tussen')

        self._schakelregime = EMAttribuut(field=StringField,
                                          naam='schakelregime',
                                          label='schakelregime',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#WV.schakelregime',
                                          definitie='Definitie nog toe te voegen voor eigenschap schakelregime')

        self._tussenafstandLed = EMAttribuut(field=StringField,
                                             naam='tussenafstand LED',
                                             label='tussenafstand LED',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#WV.tussenafstandLed',
                                             definitie='Definitie nog toe te voegen voor eigenschap tussenafstand LED')

    @property
    def gedimdTussen(self):
        """Definitie nog toe te voegen voor eigenschap gedimd tussen"""
        return self._gedimdTussen.waarde

    @gedimdTussen.setter
    def gedimdTussen(self, value):
        self._gedimdTussen.set_waarde(value, owner=self)

    @property
    def gedoofdTussen(self):
        """Definitie nog toe te voegen voor eigenschap gedoofd tussen"""
        return self._gedoofdTussen.waarde

    @gedoofdTussen.setter
    def gedoofdTussen(self, value):
        self._gedoofdTussen.set_waarde(value, owner=self)

    @property
    def schakelregime(self):
        """Definitie nog toe te voegen voor eigenschap schakelregime"""
        return self._schakelregime.waarde

    @schakelregime.setter
    def schakelregime(self, value):
        self._schakelregime.set_waarde(value, owner=self)

    @property
    def tussenafstandLed(self):
        """Definitie nog toe te voegen voor eigenschap tussenafstand LED"""
        return self._tussenafstandLed.waarde

    @tussenafstandLed.setter
    def tussenafstandLed(self, value):
        self._tussenafstandLed.set_waarde(value, owner=self)

