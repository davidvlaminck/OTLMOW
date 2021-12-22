from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVormAanleveringHoutigeVegetatie(Keuzelijst):
    """De wijze waarop het plantgoed wordt aangeleverd."""

    def __init__(self):
        super().__init__(naam="KlVormAanleveringHoutigeVegetatie",
                         label="Vorm aanlevering houtige vegetatie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormAanleveringHoutigeVegetatie",
                         definition="De wijze waarop het plantgoed wordt aangeleverd.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormAanleveringHoutigeVegetatie")

        self.add_option("poten", "poten", "Aanlevering van houtige vegetatie in de vorm van poten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/poten")
        self.add_option("bosgoed", "bosgoed", "Aanlevering van houtige vegetatie in de vorm van bosgoed.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/bosgoed")
        self.add_option("bomen", "bomen", "Aanlevering van houtige vegetatie in de vorm van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/bomen")
        self.add_option("veer", "veer", "Aanlevering van houtige vegetatie in de vorm van veer.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/veer")
        self.add_option("meerstammige-bomen", "meerstammige bomen", "Aanlevering van houtige vegetatie in de vorm van meerstammige bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/meerstammige-bomen")
