from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar(Keuzelijst):
    """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""

    def __init__(self):
        super().__init__(naam="KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar",
                         label="HS-beveiligingscel overstroombeveiliging vermogenschakelaar",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar",
                         definition="Directe of indirecte overstroombeveiliging van de vermogenschakelaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar")

        self.add_option("direct", "direct", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/direct")
        self.add_option("indirect", "indirect", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/indirect")
