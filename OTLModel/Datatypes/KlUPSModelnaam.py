# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUPSModelnaam(Keuzelijst):
    """De modelnaam van de UPS."""

    def __init__(self):
        super().__init__(naam="KlUPSModelnaam",
                         label="UPS modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUPSModelnaam",
                         definition="De modelnaam van de UPS.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUPSModelnaam")

