# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStandaardkwaliteitsklasse(Keuzelijst):
    """De mogelijke tandaardkwaliteitsklassen."""

    def __init__(self):
        super().__init__(naam="KlStandaardkwaliteitsklasse",
                         label="Standaardkwaliteitsklasse",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStandaardkwaliteitsklasse",
                         definition="De mogelijke tandaardkwaliteitsklassen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStandaardkwaliteitsklasse")

        self.add_option("a", "a", "A", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/a")
        self.add_option("b", "b", "B", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/b")
        self.add_option("c", "c", "C", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/c")
        self.add_option("d", "d", "D", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/d")
        self.add_option("e", "e", "E", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/e")
