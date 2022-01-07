# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGPUModelnaam(Keuzelijst):
    """De modelnaam van de GPU."""

    def __init__(self):
        super().__init__(naam="KlGPUModelnaam",
                         label="GPU modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGPUModelnaam",
                         definition="De modelnaam van de GPU.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGPUModelnaam")
