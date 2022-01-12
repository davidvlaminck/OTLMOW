# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Verkeersregelaar."""

    def __init__(self):
        super().__init__(naam="KlVerkeersregelaarMerk",
                         label="verkeersregelaar merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarMerk",
                         definition="Keuzelijst met merknamen voor Verkeersregelaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarMerk")

        self.add_option("dynniq", "Dynniq", "Dynniq", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/dynniq")
        self.add_option("ko-hartog", "Ko Hartog", "Ko Hartog", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/ko-hartog")
        self.add_option("peek", "Peek", "Peek", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/peek")
        self.add_option("siemens", "Siemens", "Siemens", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/siemens")
