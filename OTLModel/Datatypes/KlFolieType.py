from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlFolieType(Keuzelijst):
    """Types van folie."""

    def __init__(self):
        super().__init__(naam="KlFolieType",
                         label="Folie type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFolieType",
                         definition="Types van folie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFolieType")

        self.add_option("folietype-1", "folietype 1", "folietype 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-1")
        self.add_option("folietype-2", "folietype 2", "folietype 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-2")
        self.add_option("folietype-3a", "folietype 3a", "folietype 3a", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-3a")
        self.add_option("folietype-3b", "folietype 3b", "folietype 3b", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-3b")
        self.add_option("folietype-3a-en-3b", "folietype 3a en 3b", "folietype 3a en 3b", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-3a-en-3b")
