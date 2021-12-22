from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEDDriverMerk(Keuzelijst):
    """Het merk van de LED-driver."""

    def __init__(self):
        super().__init__(naam="KlLEDDriverMerk",
                         label="LED-driver merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverMerk",
                         definition="Het merk van de LED-driver.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverMerk")

