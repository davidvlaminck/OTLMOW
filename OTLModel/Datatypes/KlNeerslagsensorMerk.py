from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlNeerslagsensorMerk(Keuzelijst):
    """Het merk van de neerslagsensor."""

    def __init__(self):
        super().__init__(naam="KlNeerslagsensorMerk",
                         label="Neerslagsensor merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorMerk",
                         definition="Het merk van de neerslagsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorMerk")

        self.add_option("Luft", "Luft", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorMerk/Luft")
