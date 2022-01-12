# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingVoegvulling(Keuzelijst):
    """De voegvullingen van de bestrating."""

    def __init__(self):
        super().__init__(naam="KlBestratingVoegvulling",
                         label="Bestrating voegvulling",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingVoegvulling",
                         definition="De voegvullingen van de bestrating.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingVoegvulling")

        self.add_option("granulaatmengsel-0-4", "granulaatmengsel 0-4", "granulaatmengsel 0/4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/granulaatmengsel-0-4")
        self.add_option("granulaatmengsel-0-6.3", "granulaatmengsel 0-6.3", "granulaatmengsel 0/63", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/granulaatmengsel-0-6.3")
        self.add_option("mortel-met-bouwklasse-B6-B10", "mortel met bouwklasse B6-B10", "mortel met bouwklasse B6-B10", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/mortel-met-bouwklasse-B6-B10")
        self.add_option("mortel-met-bouwklasse-BF", "mortel met bouwklasse BF", "mortel met bouwklasse BF", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/mortel-met-bouwklasse-BF")
        self.add_option("split", "split", "split", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/split")
        self.add_option("steenslag-2-4", "steenslag 2-4", "steenslag 2/4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/steenslag-2-4")
        self.add_option("steenslag-2-6.3", "steenslag 2-6.3", "steenslag 2/6.3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/steenslag-2-6.3")
        self.add_option("zandcement", "zandcement", "zandcement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/zandcement")
