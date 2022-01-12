# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSteenslagType(Keuzelijst):
    """Steenslag types."""

    def __init__(self):
        super().__init__(naam="KlSteenslagType",
                         label="Steenslag type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSteenslagType",
                         definition="Steenslag types.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSteenslagType")

        self.add_option("type-IA", "type IA", "type IA", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IA")
        self.add_option("type-IB", "type IB", "type IB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IB")
        self.add_option("type-IIA", "type IIA", "type IIA", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIA")
        self.add_option("type-IIB", "type IIB", "type IIB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIB")
        self.add_option("type-IIIA", "type IIIA", "type IIIA", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIA")
        self.add_option("type-IIIB", "type IIIB", "type IIIB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIB")
