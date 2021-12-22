from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWeegsensorType(Keuzelijst):
    """Het type van de weegsensor."""

    def __init__(self):
        super().__init__(naam="KlWeegsensorType",
                         label="Weegsensor type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorType",
                         definition="Het type van de weegsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorType")

        self.add_option("piëzo-kwarts", "piëzo-kwarts", "piëzo-kwarts", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorType/piëzo-kwarts")
