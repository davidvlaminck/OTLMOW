# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarModelnaam(Keuzelijst):
    """Keuzelijst met modelnamen voor Verkeersregelaar."""

    def __init__(self):
        super().__init__(naam="KlVerkeersregelaarModelnaam",
                         label="verkeersregelaar modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarModelnaam",
                         definition="Keuzelijst met modelnamen voor Verkeersregelaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarModelnaam")

        self.add_option("flow-node", "FlowNode", "FlowNode", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/flow-node")
        self.add_option("civa-2020", "CIVA 2020", "CIVA 2020", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/civa-2020")
