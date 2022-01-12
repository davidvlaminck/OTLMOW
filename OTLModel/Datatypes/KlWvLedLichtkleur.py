# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedLichtkleur(Keuzelijst):
    """Beschrijving van de kleur van het licht adhv de naam van de kleur."""

    def __init__(self):
        super().__init__(naam="KlWvLedLichtkleur",
                         label="WV LED lichtkleur",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtkleur",
                         definition="Beschrijving van de kleur van het licht adhv de naam van de kleur.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedLichtkleur")

        self.add_option("amber", "amber", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/amber")
        self.add_option("blauw", "blauw", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/blauw")
        self.add_option("rood", "rood", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/rood")
        self.add_option("wit", "wit", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/wit")
