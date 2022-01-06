# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantopsluitingKleur(Keuzelijst):
    """De kleur van de kantopsluiting."""

    def __init__(self):
        super().__init__(naam="KlLEKantopsluitingKleur",
                         label="Kantopsluiting kleur",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantopsluitingKleur",
                         definition="De kleur van de kantopsluiting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantopsluitingKleur")

        self.add_option("zwart", "zwart", "zwart", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/zwart")
        self.add_option("wit", "wit", "wit", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/wit")
        self.add_option("oker", "oker", "oker", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/oker")
        self.add_option("rood", "rood", "rood", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/rood")
        self.add_option("grijs", "grijs", "grijs", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/grijs")
        self.add_option("gekleurd", "gekleurd", "gekleurd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/gekleurd")
