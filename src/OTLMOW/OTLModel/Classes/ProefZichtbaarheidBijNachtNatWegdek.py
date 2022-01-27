# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijNachtNatWegdek(Proef):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht bij nat wegdek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtNatWegdek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._retrotreflectiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                        naam='retrotreflectiecoëfficiënt',
                                                        label='retrotreflectiecoëfficiënt',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtNatWegdek.retrotreflectiecoëfficiënt',
                                                        usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                        definition='De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat wegdek.')

    @property
    def retrotreflectiecoëfficiënt(self):
        """De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat wegdek."""
        return self._retrotreflectiecoëfficiënt.waarde

    @retrotreflectiecoëfficiënt.setter
    def retrotreflectiecoëfficiënt(self, value):
        self._retrotreflectiecoëfficiënt.set_waarde(value, owner=self)
