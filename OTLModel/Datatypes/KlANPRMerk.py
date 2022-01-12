# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRMerk(Keuzelijst):
    """Het merk van de ANPR-camera."""

    def __init__(self):
        super().__init__(naam="KlANPRMerk",
                         label="ANPR-camera merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRMerk",
                         definition="Het merk van de ANPR-camera.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRMerk")

        self.add_option("Macq", "Macq", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Macq")
        self.add_option("Tattile", "Tattile", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Tattile")
