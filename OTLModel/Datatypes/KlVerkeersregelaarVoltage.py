from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVerkeersregelaarVoltage(Keuzelijst):
    """Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars."""

    def __init__(self):
        super().__init__(naam="KlVerkeersregelaarVoltage",
                         label="Verkeersregelaar voltage",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarVoltage",
                         definition="Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarVoltage")

        self.add_option("42", "42", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/42")
        self.add_option("230", "230", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/230")
        self.add_option("40", "40", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/40")
