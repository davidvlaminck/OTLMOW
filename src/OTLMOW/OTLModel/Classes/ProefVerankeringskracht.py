# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerankeringskracht(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Een trekproef in situ om de verankering van de ankerstaven in een betonverharding te testen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._verankeringskracht = OTLAttribuut(field=DtcDocument,
                                                naam='verankeringskracht',
                                                label='verankeringskracht',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht.verankeringskracht',
                                                definition='Het resultaat van de test om de verankeringskracht in de BV laag.',
                                                owner=self)

    @property
    def verankeringskracht(self):
        """Het resultaat van de test om de verankeringskracht in de BV laag."""
        return self._verankeringskracht.waarde

    @verankeringskracht.setter
    def verankeringskracht(self, value):
        self._verankeringskracht.set_waarde(value, owner=self)
