# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkTechnologie(Keuzelijst):
    """Lijst van mogelijke intern gebruikte netwerk protocollen."""

    def __init__(self):
        super().__init__(naam="KlNetwerkTechnologie",
                         label="Netwerk technologie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkTechnologie",
                         definition="Lijst van mogelijke intern gebruikte netwerk protocollen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkTechnologie")

        self.add_option("SDH", "SDH", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/SDH")
        self.add_option("OTN", "OTN", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/OTN")
        self.add_option("CEN", "CEN", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/CEN")
        self.add_option("WDM", "WDM", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/WDM")
        self.add_option("PDH", "PDH", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/PDH")
        self.add_option("Wireless", "Wireless", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/Wireless")
        self.add_option("Other", "Other", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/Other")
        self.add_option("NULL", "NULL", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/NULL")
