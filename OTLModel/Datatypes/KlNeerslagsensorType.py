from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlNeerslagsensorType(Keuzelijst):
    """Het type van de neerslagsensor."""

    def __init__(self):
        super().__init__(naam="KlNeerslagsensorType",
                         label="Neerslagsensor type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorType",
                         definition="Het type van de neerslagsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorType")

        self.add_option("radar", "radar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/radar")
        self.add_option("optisch", "optisch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/optisch")
