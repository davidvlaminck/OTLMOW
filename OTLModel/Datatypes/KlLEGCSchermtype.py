from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEGCSchermtype(Keuzelijst):
    """De mogelijke schermtypes (vlak, niet-vlak)."""

    def __init__(self):
        super().__init__(naam="KlLEGCSchermtype",
                         label="Schermtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermtype",
                         definition="De mogelijke schermtypes (vlak, niet-vlak).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermtype")

        self.add_option("vlak", "vlak", "De vlakke schermen zijn de schermen die kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermtype/vlak")
        self.add_option("niet-vlak", "niet-vlak", "De niet-vlakke schermen zijn de schermen die niet kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermtype/niet-vlak")
