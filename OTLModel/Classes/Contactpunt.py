# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlContactpuntType import KlContactpuntType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contactpunt(AIMObject):
    """Techniek voor het meten van een aan- of afwezigheid van contact tussen de onderdelen waaraan deze bevestigd is. """

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type contactpunt",
                                    lijst=KlContactpuntType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt.type",
                                    definition="Typering van de gebruikte techniek op basis waarvan de aan- of afwezigheid van een contact vastgesteld wordt.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Typering van de gebruikte techniek op basis waarvan de aan- of afwezigheid van een contact vastgesteld wordt."""
