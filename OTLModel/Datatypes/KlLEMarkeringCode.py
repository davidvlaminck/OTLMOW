# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEMarkeringCode(Keuzelijst):
    """Codes van de markering op lijnvormige elementen."""

    def __init__(self):
        super().__init__(naam="KlLEMarkeringCode",
                         label="Markering code",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEMarkeringCode",
                         definition="Codes van de markering op lijnvormige elementen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEMarkeringCode")

        self.add_option("DIV-BIG", "DIV-BIG", "De code voor LE markering biggenrug", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BIG")
        self.add_option("DIV-BRDSTN", "DIV-BRDSTN", "De code voor LE markering boordsteen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BRDSTN")
        self.add_option("DIV-BRDSTN-PV", "DIV-BRDSTN-PV", "De code voor LE markering boordsteen parkeerverbod", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BRDSTN-PV")
        self.add_option("DIV-NJ", "DIV-NJ", "De code voor LE markering New Jersey", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-NJ")
