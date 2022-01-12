# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorModelnaam(Keuzelijst):
    """De modelnaam van de weegsensor."""

    def __init__(self):
        super().__init__(naam="KlWeegsensorModelnaam",
                         label="Weegsensor modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorModelnaam",
                         definition="De modelnaam van de weegsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorModelnaam")

