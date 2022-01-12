# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarVoltage(Keuzelijst):
    """Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars."""

    def __init__(self):
        super().__init__(naam="KlVerkeersregelaarVoltage",
                         label="Verkeersregelaar voltage",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarVoltage",
                         definition="Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarVoltage")

        self.add_option("230", "230", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/230")
        self.add_option("40", "40", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/40")
        self.add_option("42", "42", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/42")
