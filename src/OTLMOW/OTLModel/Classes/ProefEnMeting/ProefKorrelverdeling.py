# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKorrelverdeling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de doorval door een reeks zeven van een granulaatmengsel volgens NBN EN 933-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._korrelverdeling = OTLAttribuut(field=DtcDocument,
                                             naam='korrelverdeling',
                                             label='korrelverdeling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling.korrelverdeling',
                                             definition='Het resultaat van de test van de gemeten korrelverdeling in de BV laag.',
                                             owner=self)

    @property
    def korrelverdeling(self):
        """Het resultaat van de test van de gemeten korrelverdeling in de BV laag."""
        return self._korrelverdeling.get_waarde()

    @korrelverdeling.setter
    def korrelverdeling(self, value):
        self._korrelverdeling.set_waarde(value, owner=self)
