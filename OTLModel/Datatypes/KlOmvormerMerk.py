# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerMerk(Keuzelijst):
    """Het merk van de omvormer."""

    def __init__(self):
        super().__init__(naam="KlOmvormerMerk",
                         label="Omvormer merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerMerk",
                         definition="Het merk van de omvormer.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerMerk")

        self.add_option("axis", "Axis", "Axis", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/axis")
        self.add_option("bosch", "Bosch", "Bosch", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/bosch")
