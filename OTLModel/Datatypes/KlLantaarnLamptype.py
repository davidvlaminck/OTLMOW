from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLantaarnLamptype(Keuzelijst):
    """Keuzelijst met LantaarnLamp types."""

    def __init__(self):
        super().__init__(naam="KlLantaarnLamptype",
                         label="Lantaarn lamptype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLantaarnLamptype",
                         definition="Keuzelijst met LantaarnLamp types.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLantaarnLamptype")

        self.add_option("LED", "LED", "Led lamp.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/LED")
        self.add_option("gloeilamp", "gloeilamp", "Gloeilamp.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/gloeilamp")
        self.add_option("gasontlading", "gasontlading", "Lamp op basis van gas.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/gasontlading")
        self.add_option("halogeen", "halogeen", "Halogeenlamp.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/halogeen")
