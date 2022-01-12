# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEWatergreppelType(Keuzelijst):
    """Types van watergreppel."""

    def __init__(self):
        super().__init__(naam="KlLEWatergreppelType",
                         label="Watergreppel type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEWatergreppelType",
                         definition="Types van watergreppel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEWatergreppelType")

        self.add_option("type-II-A-2", "type II A 2", "type II A 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-A-2")
        self.add_option("type-II-B-2", "type II B 2", "type II B 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-B-2")
        self.add_option("type-II-C-2", "type II C 2", "type II C 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-C-2")
        self.add_option("type-II-D-2", "type II D 2", "type II D 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-D-2")
        self.add_option("type-II-E-2", "type II E 2", "type II E 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-E-2")
