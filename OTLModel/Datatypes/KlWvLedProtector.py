from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWvLedProtector(Keuzelijst):
    """Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."""

    def __init__(self):
        super().__init__(naam="KlWvLedProtector",
                         label="WV protector",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedProtector",
                         definition="Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedProtector")

        self.add_option("vlak-glas", "vlak glas", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/vlak-glas")
        self.add_option("gebogen-glas", "gebogen glas", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/gebogen-glas")
        self.add_option("polycarbonaat", "polycarbonaat", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/polycarbonaat")
