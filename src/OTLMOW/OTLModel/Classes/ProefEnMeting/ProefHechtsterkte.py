# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefHechtsterkte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Het resultaat van de trekproef waarbij een proefstuk wordt blootgesteld aan een stijgende spanning tot er een breuk optreedt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._hechtsterkte = OTLAttribuut(field=DtcDocument,
                                          naam='hechtsterkte',
                                          label='hechtsterkte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte.hechtsterkte',
                                          definition='Proef om de hechtsterkte van de laag te bepalen.',
                                          owner=self)

    @property
    def hechtsterkte(self):
        """Proef om de hechtsterkte van de laag te bepalen."""
        return self._hechtsterkte.get_waarde()

    @hechtsterkte.setter
    def hechtsterkte(self, value):
        self._hechtsterkte.set_waarde(value, owner=self)
