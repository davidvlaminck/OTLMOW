# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Buis import Buis
from OTLModel.Datatypes.KlPersleidingMateriaal import KlPersleidingMateriaal
from OTLModel.Datatypes.KlSDRKlasse import KlSDRKlasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class Persleiding(Buis):
    """Ondergronds kanaal of pijp voor afvoer van een vloeistof of gas onder druk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaal = OTLAttribuut(field=KlPersleidingMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.materiaal',
                                       definition='Bepaalt het materiaal van de persleiding.')

        self._sdrKlasse = OTLAttribuut(field=KlSDRKlasse,
                                       naam='sdrKlasse',
                                       label='SDR klasse',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.sdrKlasse',
                                       definition='De verhouding tussen de wanddikte en de diameter van de persleiding.')

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de persleiding."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sdrKlasse(self):
        """De verhouding tussen de wanddikte en de diameter van de persleiding."""
        return self._sdrKlasse.waarde

    @sdrKlasse.setter
    def sdrKlasse(self, value):
        self._sdrKlasse.set_waarde(value, owner=self)
