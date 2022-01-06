# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTransformatorTrafobeveiliging(Keuzelijst):
    """Type transformatorbeveiliging."""

    def __init__(self):
        super().__init__(naam="KlTransformatorTrafobeveiliging",
                         label="Transformator trafobeveiliging",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTransformatorTrafobeveiliging",
                         definition="Type transformatorbeveiliging.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTransformatorTrafobeveiliging")

        self.add_option("overtemperatuur", "overtemperatuur", "attributen invullen//", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overtemperatuur")
        self.add_option("overdruk", "overdruk", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overdruk")
        self.add_option("gecombineerd", "gecombineerd", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/gecombineerd")
