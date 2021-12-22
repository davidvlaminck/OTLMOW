from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVegetatieDrassigheid(Keuzelijst):
    """De mate van drassigheid.."""

    def __init__(self):
        super().__init__(naam="KlVegetatieDrassigheid",
                         label="Vegetatie drassigheid",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieDrassigheid",
                         definition="De mate van drassigheid..",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieDrassigheid")

        self.add_option("matig-drassig", "matig drassig", "De ondergrond is matig drassig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/matig-drassig")
        self.add_option("niet-drassig", "niet drassig", "De ondergrond is niet drassig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/niet-drassig")
        self.add_option("sterk-drassig", "sterk drassig", "De ondergrond is sterk drassig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/sterk-drassig")
