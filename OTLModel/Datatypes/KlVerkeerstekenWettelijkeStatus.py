from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVerkeerstekenWettelijkeStatus(Keuzelijst):
    """Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven."""

    def __init__(self):
        super().__init__(naam="KlVerkeerstekenWettelijkeStatus",
                         label="VerkeerstekenWettelijkeStatus",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeerstekenWettelijkeStatus",
                         definition="Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven.",
                         usagenote="Bijvoorbeeld: vergund, niet-vergund, in ontwerp",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerstekenWettelijkeStatus")

