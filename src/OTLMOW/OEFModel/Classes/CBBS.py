# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class CBBS(EMObject):
    """Centraal Bedienings- en Bewakingssysteem (voor Kunstwerken)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#CBBS'
    label = 'Centrale bediening bewakingssysteem'

    def __init__(self):
        super().__init__()

        self._kabelkelderVrijVanWater = EMAttribuut(field=StringField,
                                                    naam='kabelkelder vrij van water',
                                                    label='kabelkelder vrij van water',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.kabelkelderVrijVanWater',
                                                    definitie='Definitie nog toe te voegen voor eigenschap kabelkelder vrij van water',
                                                    owner=self)

    @property
    def kabelkelderVrijVanWater(self):
        """Definitie nog toe te voegen voor eigenschap kabelkelder vrij van water"""
        return self._kabelkelderVrijVanWater.waarde

    @kabelkelderVrijVanWater.setter
    def kabelkelderVrijVanWater(self, value):
        self._kabelkelderVrijVanWater.set_waarde(value, owner=self)

