# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class AntiParkeerpaalType(Keuzelijst):
    """De vormen van een anti-parkeerpaal."""

    def __init__(self):
        super().__init__(naam="AntiParkeerpaalType",
                         label="Anti-parkeerpaal type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaalType",
                         definition="De vormen van een anti-parkeerpaal.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/AntiParkeerpaalType")

        self.add_option("conischeTrottoirpaalAmsterdammer", "conischeTrottoirpaalAmsterdammer", "Conische paal met afgeronde kop en sierring.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/AntiParkeerpaalType/conischeTrottoirpaalAmsterdammer")
        self.add_option("diamantkoppaal", "diamantkoppaal", "Een paal voorzien van een diamantkop en op de hoeken 4 vellingkanten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/AntiParkeerpaalType/diamantkoppaal")
