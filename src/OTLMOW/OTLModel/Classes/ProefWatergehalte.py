# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWatergehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de hoeveelheid water die opgenomen kan worden in een betonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._watergehalte = OTLAttribuut(field=DtcDocument,
                                          naam='watergehalte',
                                          label='watergehalte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte.watergehalte',
                                          definition='Het resultaat van de test van het gemeten watergehalte in de BV laag.',
                                          owner=self)

    @property
    def watergehalte(self):
        """Het resultaat van de test van het gemeten watergehalte in de BV laag."""
        return self._watergehalte.get_waarde()

    @watergehalte.setter
    def watergehalte(self, value):
        self._watergehalte.set_waarde(value, owner=self)
