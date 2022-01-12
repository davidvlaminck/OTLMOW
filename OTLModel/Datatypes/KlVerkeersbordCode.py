# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordCode(Keuzelijst):
    """De code van het verkeersbord volgens de wegcode."""

    def __init__(self):
        super().__init__(naam="KlVerkeersbordCode",
                         label="Verkeersbordcode",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordCode",
                         definition="De code van het verkeersbord volgens de wegcode.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordCode")

        self.add_option("F34b1", "F34b1", "F34b1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34b1")
        self.add_option("F34b2", "F34b2", "F34b2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34b2")
        self.add_option("F34c", "F34c", "F34c", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34c")
        self.add_option("F35", "F35", "F35", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F35")
        self.add_option("F37", "F37", "F37", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F37")
        self.add_option("F67", "F67", "F67", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F67")
