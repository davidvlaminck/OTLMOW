# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantstrookType(Keuzelijst):
    """Types van kantstrook."""

    def __init__(self):
        super().__init__(naam="KlLEKantstrookType",
                         label="Kantstrook type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantstrookType",
                         definition="Types van kantstrook.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantstrookType")

        self.add_option("type-II-A-1", "type II A 1", "type II A 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-A-1")
        self.add_option("type-II-B-1", "type II B 1", "type II B 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-B-1")
        self.add_option("type-II-C-1", "type II C 1", "type II C 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-C-1")
        self.add_option("type-II-D-1", "type II D 1", "type II D 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-D-1")
        self.add_option("type-II-E-1", "type II E 1", "type II E 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-E-1")
