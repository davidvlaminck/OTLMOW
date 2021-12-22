from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBestratingSteenverband(Keuzelijst):
    """De steenverbanden van de bestrating."""

    def __init__(self):
        super().__init__(naam="KlBestratingSteenverband",
                         label="Bestrating steenverband",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingSteenverband",
                         definition="De steenverbanden van de bestrating.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingSteenverband")

        self.add_option("segmentverband", "segmentverband", "Segmentverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/segmentverband")
        self.add_option("schubbenverband", "schubbenverband", "Schubbenverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schubbenverband")
        self.add_option("waaierverband", "waaierverband", "Waaierverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/waaierverband")
        self.add_option("schelpen--of-pauwstaartverband", "schelpen- of pauwstaartverband", "Schelpen- of pauwstaartverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schelpen--of-pauwstaartverband")
        self.add_option("halfsteensverband", "halfsteensverband", "Halfsteensverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/halfsteensverband")
        self.add_option("elleboogverband", "elleboogverband", "Elleboogverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/elleboogverband")
        self.add_option("visgraatverband", "visgraatverband", "Visgraatverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/visgraatverband")
        self.add_option("keperverband", "keperverband", "Keperverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/keperverband")
        self.add_option("blokverband", "blokverband", "Blokverband", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/blokverband")
