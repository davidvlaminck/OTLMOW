# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefMortelkwaliteit(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de sterkte van voegmortel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._mortelkwaliteit = OTLAttribuut(field=DtcDocument,
                                             naam='mortelkwaliteit',
                                             label='mortelkwaliteit',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit.mortelkwaliteit',
                                             definition='Een rapport van de mortelkwaliteit van de onderbouw laag.',
                                             owner=self)

    @property
    def mortelkwaliteit(self):
        """Een rapport van de mortelkwaliteit van de onderbouw laag."""
        return self._mortelkwaliteit.waarde

    @mortelkwaliteit.setter
    def mortelkwaliteit(self, value):
        self._mortelkwaliteit.set_waarde(value, owner=self)
