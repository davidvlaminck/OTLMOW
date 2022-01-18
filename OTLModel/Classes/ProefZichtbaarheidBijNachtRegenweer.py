# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijNachtRegenweer(Proef, AttributeInfo):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht bij nat weer (tijdens regenbui)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtRegenweer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._retrotreflectiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                        naam='retrotreflectiecoëfficiënt',
                                                        label='retrotreflectiecoëfficiënt',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtRegenweer.retrotreflectiecoëfficiënt',
                                                        usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                        definition='De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat weer (tijdens regenbui).')

    @property
    def retrotreflectiecoëfficiënt(self):
        """De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat weer (tijdens regenbui)."""
        return self._retrotreflectiecoëfficiënt.waarde

    @retrotreflectiecoëfficiënt.setter
    def retrotreflectiecoëfficiënt(self, value):
        self._retrotreflectiecoëfficiënt.set_waarde(value, owner=self)
