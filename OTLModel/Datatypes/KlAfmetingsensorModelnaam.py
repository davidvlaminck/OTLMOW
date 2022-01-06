# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorModelnaam(Keuzelijst):
    """De modelnaam van de afmetingsensor."""

    def __init__(self):
        super().__init__(naam="KlAfmetingsensorModelnaam",
                         label="Afmetingsensor modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorModelnaam",
                         definition="De modelnaam van de afmetingsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorModelnaam")

        self.add_option("LMS", "LMS", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/LMS")
        self.add_option("FPS", "FPS", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/FPS")
