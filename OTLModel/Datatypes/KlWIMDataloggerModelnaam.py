# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWIMDataloggerModelnaam(Keuzelijst):
    """De modelnaam van de WIM-datalogger."""

    def __init__(self):
        super().__init__(naam="KlWIMDataloggerModelnaam",
                         label="WIM-datalogger modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWIMDataloggerModelnaam",
                         definition="De modelnaam van de WIM-datalogger.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWIMDataloggerModelnaam")

