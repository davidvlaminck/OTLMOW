# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurPlooibaken(Keuzelijst):
    """Kleuropties voor het plooibaken."""

    def __init__(self):
        super().__init__(naam="KlKleurPlooibaken",
                         label="Kleur plooibaken",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurPlooibaken",
                         definition="Kleuropties voor het plooibaken.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurPlooibaken")

        self.add_option("blauw", "blauw", "blauw", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/blauw")
        self.add_option("geel", "geel", "geel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/geel")
        self.add_option("grijs", "grijs", "grijs", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/grijs")
        self.add_option("groen", "groen", "groen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/groen")
        self.add_option("oranje", "oranje", "oranje", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/oranje")
        self.add_option("rood", "rood", "rood", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/rood")
        self.add_option("zwart", "zwart", "zwart", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/zwart")
