# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerModelnaam(Keuzelijst):
    """De modelnaam van de omvormer."""

    def __init__(self):
        super().__init__(naam="KlOmvormerModelnaam",
                         label="Omvormer modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerModelnaam",
                         definition="De modelnaam van de omvormer.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerModelnaam")

