# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurReflector(Keuzelijst):
    """Kleuropties voor de reflector."""

    def __init__(self):
        super().__init__(naam="KlKleurReflector",
                         label="Kleur reflector",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurReflector",
                         definition="Kleuropties voor de reflector.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurReflector")

        self.add_option("amber", "amber", "amber", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurReflector/amber")
        self.add_option("blauw", "blauw", "blauw", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurReflector/blauw")
        self.add_option("groen", "groen", "groen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurReflector/groen")
        self.add_option("rood", "rood", "rood", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurReflector/rood")
        self.add_option("wit", "wit", "wit", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurReflector/wit")
