# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.KlKopmuurMateriaal import KlKopmuurMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kopmuur(AIMObject):
    """Een kopmuur is een inrichtingselement van de wegbaan, dat gebruikt wordt voor de geleiding van verkeer bij grachten. Een kopmuur is een keermuur die een functie vervult van afwateringssysteem en is in de regel haaks op de hartlijn van de wegcorridor georiënteerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaal = OTLAttribuut(field=KlKopmuurMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur.materiaal',
                                       definition='Bepaalt het materiaal van de kopmuur.')

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de kopmuur."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
