# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeergegevenVervoersmodiOpKaart(Keuzelijst):
    """De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden meegegeven."""

    def __init__(self):
        super().__init__(naam="KlWeergegevenVervoersmodiOpKaart",
                         label="Weergegeven vervoersmodi op kaart",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeergegevenVervoersmodiOpKaart",
                         definition="De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden meegegeven.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeergegevenVervoersmodiOpKaart")

        self.add_option("deelauto", "Deelauto", "TODO", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/deelauto")
        self.add_option("deelfiets", "Deelfiets", "TODO", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/deelfiets")
        self.add_option("flexvervoer", "Flexvervoer", "TODO", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/flexvervoer")
        self.add_option("kernnet-aanvullend-net", "Kernnet - aanvullend net", "TODO", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/kernnet-aanvullend-net")
        self.add_option("treinnet", "Treinnet", "TODO", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/treinnet")
        self.add_option("vast-en-semiflex", "Vast en semiflex", "TODO", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/vast-en-semiflex")
