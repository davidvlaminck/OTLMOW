# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef die de hoeveelheid lucht bepaalt  in vers beton met de drukmethode volgens NBN EN 12350-7."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._luchtgehalte = OTLAttribuut(field=DtcDocument,
                                          naam='luchtgehalte',
                                          label='luchtgehalte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte.luchtgehalte',
                                          definition='Proefresultaten van het luchtgehalte.',
                                          owner=self)

    @property
    def luchtgehalte(self):
        """Proefresultaten van het luchtgehalte."""
        return self._luchtgehalte.waarde

    @luchtgehalte.setter
    def luchtgehalte(self, value):
        self._luchtgehalte.set_waarde(value, owner=self)
