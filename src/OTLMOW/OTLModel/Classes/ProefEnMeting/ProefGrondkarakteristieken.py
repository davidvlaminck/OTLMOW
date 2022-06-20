# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGrondkarakteristieken(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de grondeigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._bepalingGrondkarakteristieken = OTLAttribuut(field=DtcDocument,
                                                           naam='bepalingGrondkarakteristieken',
                                                           label='bepaling grondkarakteristieken',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken.bepalingGrondkarakteristieken',
                                                           definition='Proef met de resultaten van de grondkarakteristieken.',
                                                           owner=self)

    @property
    def bepalingGrondkarakteristieken(self):
        """Proef met de resultaten van de grondkarakteristieken."""
        return self._bepalingGrondkarakteristieken.get_waarde()

    @bepalingGrondkarakteristieken.setter
    def bepalingGrondkarakteristieken(self, value):
        self._bepalingGrondkarakteristieken.set_waarde(value, owner=self)
