from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEACSchokindexMVP(Keuzelijst):
    """Head injury criteria (HIC) van een motorvangplank."""

    def __init__(self):
        super().__init__(naam="KlLEACSchokindexMVP",
                         label="Schokindex MVP",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSchokindexMVP",
                         definition="Head injury criteria (HIC) van een motorvangplank.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSchokindexMVP")

        self.add_option("level-1", "level 1", "Krachten op hoofd en nek worden beperkt tijdens test", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindexMVP/level-1")
        self.add_option("level-2", "level 2", "Krachten op hoofd en nek worden tot levensgevaarlijk tijdens test", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindexMVP/level-2")
