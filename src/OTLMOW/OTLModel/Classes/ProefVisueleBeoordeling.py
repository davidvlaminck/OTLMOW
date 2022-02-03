# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVisueleBeoordeling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Opsporen van de gebreken bij de definitieve oplevering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._visueleBeoordeling = OTLAttribuut(field=DtcDocument,
                                                naam='visueleBeoordeling',
                                                label='visuele beoordeling',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling.visueleBeoordeling',
                                                definition='Een rapport van de visuele beoordeling van de laag.',
                                                owner=self)

    @property
    def visueleBeoordeling(self):
        """Een rapport van de visuele beoordeling van de laag."""
        return self._visueleBeoordeling.waarde

    @visueleBeoordeling.setter
    def visueleBeoordeling(self, value):
        self._visueleBeoordeling.set_waarde(value, owner=self)
