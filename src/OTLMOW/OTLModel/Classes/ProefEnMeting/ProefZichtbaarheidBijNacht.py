# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijNacht(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._retrotreflectiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                        naam='retrotreflectiecoëfficiënt',
                                                        label='retrotreflectiecoëfficiënt',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht.retrotreflectiecoëfficiënt',
                                                        usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                        definition='De maat voor het retroreflecterend vermogen van een markering bij nacht.',
                                                        owner=self)

    @property
    def retrotreflectiecoëfficiënt(self):
        """De maat voor het retroreflecterend vermogen van een markering bij nacht."""
        return self._retrotreflectiecoëfficiënt.get_waarde()

    @retrotreflectiecoëfficiënt.setter
    def retrotreflectiecoëfficiënt(self, value):
        self._retrotreflectiecoëfficiënt.set_waarde(value, owner=self)
