# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverModelnaam(Keuzelijst):
    """De modelnaam van de LED-driver."""

    def __init__(self):
        super().__init__(naam="KlLEDDriverModelnaam",
                         label="LED-driver modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverModelnaam",
                         definition="De modelnaam van de LED-driver.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverModelnaam")

