from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlOverlangsemarkeringType(Keuzelijst):
    """Mogelijke types van de overlangse markering."""

    def __init__(self):
        super().__init__(naam="KlOverlangsemarkeringType",
                         label="Overlangse markering type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverlangsemarkeringType",
                         definition="Mogelijke types van de overlangse markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverlangsemarkeringType")

        self.add_option("onderbroken", "onderbroken", "Een overlangse markering bestaande uit een onderbroken streep.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangsemarkeringType/onderbroken")
        self.add_option("doorlopend", "doorlopend", "Een overlangse markering bestaande uit een doorlopende streep.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangsemarkeringType/doorlopend")
