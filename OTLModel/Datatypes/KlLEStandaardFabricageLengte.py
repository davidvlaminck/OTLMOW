from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEStandaardFabricageLengte(Keuzelijst):
    """De lengte van de inviduele kantopsluiting volgens de norm."""

    def __init__(self):
        super().__init__(naam="KlLEStandaardFabricageLengte",
                         label="Standaard frabricage lengte",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEStandaardFabricageLengte",
                         definition="De lengte van de inviduele kantopsluiting volgens de norm.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEStandaardFabricageLengte")

        self.add_option("0.5-m", "0,5 m", "De fabricagelengte is 0,5 meter.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEStandaardFabricageLengte/0.5-m")
        self.add_option("1-m", "1 m", "De fabricagelengte is 1 meter.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEStandaardFabricageLengte/1-m")
