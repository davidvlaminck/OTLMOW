from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlTypeBeschoeiing(Keuzelijst):
    """Type beschoeiing."""

    def __init__(self):
        super().__init__(naam="KlTypeBeschoeiing",
                         label="Type beschoeiing",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBeschoeiing",
                         definition="Type beschoeiing.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBeschoeiing")

        self.add_option("Krings", "Krings", "Krings", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschoeiing/Krings")
        self.add_option("Berliner", "Berliner", "Berliner", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschoeiing/Berliner")
