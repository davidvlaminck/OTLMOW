# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDraagvermogen(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de verdichting van de ondergrond of van een funderingslaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._draagvermogen = OTLAttribuut(field=DtcDocument,
                                           naam='draagvermogen',
                                           label='draagvermogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen.draagvermogen',
                                           definition='Proef die het draagvermogen van de laag bepaald.',
                                           owner=self)

    @property
    def draagvermogen(self):
        """Proef die het draagvermogen van de laag bepaald."""
        return self._draagvermogen.waarde

    @draagvermogen.setter
    def draagvermogen(self, value):
        self._draagvermogen.set_waarde(value, owner=self)
