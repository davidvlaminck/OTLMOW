# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlKopmuurMateriaal import KlKopmuurMateriaal
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kopmuur(AIMObject, VlakGeometrie):
    """Een kopmuur is een inrichtingselement van de wegbaan, dat gebruikt wordt voor de geleiding van verkeer bij grachten. Een kopmuur is een keermuur die een functie vervult van afwateringssysteem en is in de regel haaks op de hartlijn van de wegcorridor georiënteerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._materiaal = OTLAttribuut(field=KlKopmuurMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur.materiaal',
                                       definition='Bepaalt het materiaal van de kopmuur.',
                                       owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de kopmuur."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
