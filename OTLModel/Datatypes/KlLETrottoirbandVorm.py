from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLETrottoirbandVorm(Keuzelijst):
    """De vormen van een trottoirband."""

    def __init__(self):
        super().__init__(naam="KlLETrottoirbandVorm",
                         label="Trottoirband vorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandVorm",
                         definition="De vormen van een trottoirband.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandVorm")

        self.add_option("afgeschuind", "afgeschuind", "Afgeschuind", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandVorm/afgeschuind")
