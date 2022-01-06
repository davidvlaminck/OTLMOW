# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoAfschermingtype(Keuzelijst):
    """Types van afscherming."""

    def __init__(self):
        super().__init__(naam="KlEcoAfschermingtype",
                         label="Afschermingtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoAfschermingtype",
                         definition="Types van afscherming.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoAfschermingtype")

        self.add_option("houten", "houten", "Een afscherming bestaande uit houten schermen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/houten")
        self.add_option("metalen", "metalen", "Een afscherming bestaande uit metalen schermen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/metalen")
        self.add_option("heidematten", "heidematten", "Een afscherming bestaande uit heidematten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/heidematten")
