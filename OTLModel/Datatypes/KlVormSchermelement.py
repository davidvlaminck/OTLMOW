from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVormSchermelement(Keuzelijst):
    """Deze keuzelijst geeft aan of het schermelement recht of gebogen is."""

    def __init__(self):
        super().__init__(naam="KlVormSchermelement",
                         label="Vorm schermelement",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormSchermelement",
                         definition="Deze keuzelijst geeft aan of het schermelement recht of gebogen is.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormSchermelement")

        self.add_option("gebogen", "gebogen", "gebogen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/gebogen")
        self.add_option("recht", "recht", "recht", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/recht")
