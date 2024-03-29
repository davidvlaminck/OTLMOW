# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Buis import Buis
from OTLMOW.OTLModel.Datatypes.KlPersleidingMateriaal import KlPersleidingMateriaal
from OTLMOW.OTLModel.Datatypes.KlSDRKlasse import KlSDRKlasse
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Persleiding(Buis, LijnGeometrie):
    """Ondergronds kanaal of pijp voor afvoer van een vloeistof of gas onder druk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Buis.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk')

        self._materiaal = OTLAttribuut(field=KlPersleidingMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.materiaal',
                                       definition='Bepaalt het materiaal van de persleiding.',
                                       owner=self)

        self._sdrKlasse = OTLAttribuut(field=KlSDRKlasse,
                                       naam='sdrKlasse',
                                       label='SDR klasse',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.sdrKlasse',
                                       definition='De verhouding tussen de wanddikte en de diameter van de persleiding.',
                                       owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de persleiding."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sdrKlasse(self):
        """De verhouding tussen de wanddikte en de diameter van de persleiding."""
        return self._sdrKlasse.get_waarde()

    @sdrKlasse.setter
    def sdrKlasse(self, value):
        self._sdrKlasse.set_waarde(value, owner=self)
