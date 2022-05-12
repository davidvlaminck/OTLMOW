# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWeerstandAfschilfering(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de vorst-dooiweerstand volgens CEN/TS 12390-9."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._weerstandAfschilfering = OTLAttribuut(field=DtcDocument,
                                                    naam='weerstandAfschilfering',
                                                    label='weerstand afschilfering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering.weerstandAfschilfering',
                                                    definition='Proef om de weerstand/afschilfering van de laag te bepalen.',
                                                    owner=self)

    @property
    def weerstandAfschilfering(self):
        """Proef om de weerstand/afschilfering van de laag te bepalen."""
        return self._weerstandAfschilfering.get_waarde()

    @weerstandAfschilfering.setter
    def weerstandAfschilfering(self, value):
        self._weerstandAfschilfering.set_waarde(value, owner=self)
