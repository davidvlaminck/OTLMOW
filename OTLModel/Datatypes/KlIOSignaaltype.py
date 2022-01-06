# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOSignaaltype(Keuzelijst):
    """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""

    def __init__(self):
        super().__init__(naam="KlIOSignaaltype",
                         label="IO-kaart signaaltype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOSignaaltype",
                         definition="Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOSignaaltype")

        self.add_option("analoog", "analoog", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/analoog")
        self.add_option("digitaal", "digitaal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/digitaal")
