# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijNacht(Proef):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._retrotreflectiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                        naam='retrotreflectiecoëfficiënt',
                                                        label='retrotreflectiecoëfficiënt',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht.retrotreflectiecoëfficiënt',
                                                        usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                        definition='De maat voor het retroreflecterend vermogen van een markering bij nacht.')

    @property
    def retrotreflectiecoëfficiënt(self):
        """De maat voor het retroreflecterend vermogen van een markering bij nacht."""
        return self._retrotreflectiecoëfficiënt.waarde

    @retrotreflectiecoëfficiënt.setter
    def retrotreflectiecoëfficiënt(self, value):
        self._retrotreflectiecoëfficiënt.set_waarde(value, owner=self)
