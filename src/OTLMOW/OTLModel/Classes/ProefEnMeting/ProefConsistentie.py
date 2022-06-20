# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefConsistentie(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Zetmaat van betonspecie volgens NBN EN 12350-2 bij een cementbetonverharding of een lijnvormig element."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._consistentie = OTLAttribuut(field=DtcDocument,
                                          naam='consistentie',
                                          label='consistentie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie.consistentie',
                                          definition='Proefresultaten van de consistentie.',
                                          owner=self)

    @property
    def consistentie(self):
        """Proefresultaten van de consistentie."""
        return self._consistentie.get_waarde()

    @consistentie.setter
    def consistentie(self, value):
        self._consistentie.set_waarde(value, owner=self)
