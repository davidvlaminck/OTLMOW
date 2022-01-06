# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareModelnaam(Keuzelijst):
    """De modelnaam van de hardware."""

    def __init__(self):
        super().__init__(naam="KlHardwareModelnaam",
                         label="Hardware modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareModelnaam",
                         definition="De modelnaam van de hardware.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareModelnaam")

