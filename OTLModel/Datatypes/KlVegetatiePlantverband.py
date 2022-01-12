# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatiePlantverband(Keuzelijst):
    """De verschillende opties voor het plantverband."""

    def __init__(self):
        super().__init__(naam="KlVegetatiePlantverband",
                         label="Vegetatie plantverband",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatiePlantverband",
                         definition="De verschillende opties voor het plantverband.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatiePlantverband")

        self.add_option("geschrankt", "geschrankt", "De planten staan geschrankt", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/geschrankt")
        self.add_option("rijafstand", "rijafstand", "De afstand tussen de rijen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/rijafstand")
