# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLangsvlakheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De controle van de langsvlakheid nieuwe verhardingen bij verschillende golflengten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._langsvlakheid = OTLAttribuut(field=DtcDocument,
                                           naam='langsvlakheid',
                                           label='langsvlakheid',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid.langsvlakheid',
                                           definition='Het resultaat van de meting.',
                                           owner=self)

    @property
    def langsvlakheid(self):
        """Het resultaat van de meting."""
        return self._langsvlakheid.get_waarde()

    @langsvlakheid.setter
    def langsvlakheid(self, value):
        self._langsvlakheid.set_waarde(value, owner=self)
