# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAantalBoompalen(Keuzelijst):
    """Hoeveelheid palen waaruit de constructie bestaat."""

    def __init__(self):
        super().__init__(naam="KlAantalBoompalen",
                         label="Aantal boompalen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAantalBoompalen",
                         definition="Hoeveelheid palen waaruit de constructie bestaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAantalBoompalen")

        self.add_option("1", "1", "De constructie bestaat uit 1 boompaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAantalBoompalen/1")
        self.add_option("2", "2", "De constructie bestaat uit 2 boompalen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAantalBoompalen/2")
        self.add_option("3", "3", "De constructie bestaat uit 3 boompalen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAantalBoompalen/3")
