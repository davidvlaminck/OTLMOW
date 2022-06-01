# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NietGedragenSensor import NietGedragenSensor
from OTLMOW.OTLModel.Datatypes.KlDieptetemperatuurSensorMerk import KlDieptetemperatuurSensorMerk
from OTLMOW.OTLModel.Datatypes.KlDieptetemperatuursensorModelnaam import KlDieptetemperatuursensorModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dieptetemperatuursensor(NietGedragenSensor):
    """Sensor die de temperatuur meet van de ondergrond op een bepaalde diepte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieptetemperatuursensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlDieptetemperatuurSensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieptetemperatuursensor.merk',
                                  definition='Het merk van de dieptetemperatuursensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDieptetemperatuursensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieptetemperatuursensor.modelnaam',
                                       definition='De modelnaam van de dieptetemperatuursensor.',
                                       owner=self)

        self._opsteldiepte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='opsteldiepte',
                                          label='opsteldiepte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieptetemperatuursensor.opsteldiepte',
                                          definition='De diepte onder het wegdek waar de dieptesensor is opgesteld in centimeter.',
                                          owner=self)

    @property
    def merk(self):
        """Het merk van de dieptetemperatuursensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de dieptetemperatuursensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opsteldiepte(self):
        """De diepte onder het wegdek waar de dieptesensor is opgesteld in centimeter."""
        return self._opsteldiepte.get_waarde()

    @opsteldiepte.setter
    def opsteldiepte(self, value):
        self._opsteldiepte.set_waarde(value, owner=self)
