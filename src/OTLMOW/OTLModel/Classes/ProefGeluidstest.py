# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcGeluidstestRapport import DtcGeluidstestRapport
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGeluidstest(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Test van het geluidsscherm op oa. luchtgeluidsisolatie, geluidsabsorptie, e.d. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._geluidstestrapport = OTLAttribuut(field=DtcGeluidstestRapport,
                                                naam='geluidstestrapport',
                                                label='geluidstestrapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest.geluidstestrapport',
                                                definition='Het resultaat geluidstest.',
                                                owner=self)

    @property
    def geluidstestrapport(self):
        """Het resultaat geluidstest."""
        return self._geluidstestrapport.waarde

    @geluidstestrapport.setter
    def geluidstestrapport(self, value):
        self._geluidstestrapport.set_waarde(value, owner=self)
