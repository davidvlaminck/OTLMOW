from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEGCNorm(Keuzelijst):
    """De mogelijke normen."""

    def __init__(self):
        super().__init__(naam="KlLEGCNorm",
                         label="Norm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCNorm",
                         definition="De mogelijke normen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCNorm")

        self.add_option("NBN-EN-1793-1", "NBN EN 1793-1", "Beproevingsmethode deel 1 'Intrinsieke kenmerken van de geluidabsorptie'", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-1")
        self.add_option("NBN-EN-1793-2", "NBN EN 1793-2", "Beproevingsmethode deel 2 'Intrinsieke kenmerken van de luchtgeluidisolatie'", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-2")
        self.add_option("NBN-EN-1793-5", "NBN EN 1793-5", "Beproevingsmethode deel 5 'Intrinsieke kenmerken - In situ waarden van geluidsisolatie onder directe geluidveld omstandigheden'", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-5")
        self.add_option("NBN-EN-1793-6", "NBN EN 1793-6", "Beproevingsmethode deel 6 'In-situ waarden van luchtgeluidisolatie onder directe geluidsveldcondities'", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-6")
