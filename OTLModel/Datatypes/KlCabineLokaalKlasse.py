from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlCabineLokaalKlasse(Keuzelijst):
    """Lijst van waarden voor de classificatie van de hoogspanningscabine als lokaal volgens Synergrid."""

    def __init__(self):
        super().__init__(naam="KlCabineLokaalKlasse",
                         label="Cabine lokaal klasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineLokaalKlasse",
                         definition="Lijst van waarden voor de classificatie van de hoogspanningscabine als lokaal volgens Synergrid.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineLokaalKlasse")

        self.add_option("BB00", "BB00", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB00")
        self.add_option("BB05", "BB05", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB05")
        self.add_option("BB10", "BB10", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB10")
        self.add_option("BB20", "BB20", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB20")
        self.add_option("BB40", "BB40", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB40")
        self.add_option("BB30", "BB30", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB30")
        self.add_option("BB50", "BB50", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB50")
