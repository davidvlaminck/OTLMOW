# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class Z30Paal(EMObject):
    """Dynamische borden : individueel zone30 bord met bijhorende paal, subonderdeel van zone30-installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Z30Paal'
    label = 'Zone30 paal'

    def __init__(self):
        super().__init__()

        self._bordType = EMAttribuut(field=StringField,
                                     naam='Bord Type',
                                     label='Bord Type',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Z30Paal.bordType',
                                     definitie='Bord Type')

        self._genummerdeWeg = EMAttribuut(field=BooleanField,
                                          naam='Genummerde Weg',
                                          label='Genummerde Weg',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Z30Paal.genummerdeWeg',
                                          definitie='Genummerde Weg')

        self._producent = EMAttribuut(field=StringField,
                                      naam='Producent',
                                      label='Producent',
                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Z30Paal.producent',
                                      definitie='Producent')

    @property
    def bordType(self):
        """Bord Type"""
        return self._bordType.waarde

    @bordType.setter
    def bordType(self, value):
        self._bordType.set_waarde(value, owner=self)

    @property
    def genummerdeWeg(self):
        """Genummerde Weg"""
        return self._genummerdeWeg.waarde

    @genummerdeWeg.setter
    def genummerdeWeg(self, value):
        self._genummerdeWeg.set_waarde(value, owner=self)

    @property
    def producent(self):
        """Producent"""
        return self._producent.waarde

    @producent.setter
    def producent(self, value):
        self._producent.set_waarde(value, owner=self)

