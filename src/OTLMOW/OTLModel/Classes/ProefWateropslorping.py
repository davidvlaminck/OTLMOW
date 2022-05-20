# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWateropslorping(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef waarbij de compactheid of poreusheid van het proefstuk door onderdompeling wordt bepaald."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._wateropslorping = OTLAttribuut(field=DtcDocument,
                                             naam='wateropslorping',
                                             label='wateropslorping',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping.wateropslorping',
                                             definition='Proef om de wateropslorping van de laag te bepalen.',
                                             owner=self)

    @property
    def wateropslorping(self):
        """Proef om de wateropslorping van de laag te bepalen."""
        return self._wateropslorping.get_waarde()

    @wateropslorping.setter
    def wateropslorping(self, value):
        self._wateropslorping.set_waarde(value, owner=self)
