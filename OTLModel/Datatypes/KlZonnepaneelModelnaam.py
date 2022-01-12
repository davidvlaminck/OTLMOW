# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonnepaneelModelnaam(Keuzelijst):
    """De modelnaam van het zonnepaneel."""

    def __init__(self):
        super().__init__(naam="KlZonnepaneelModelnaam",
                         label="Zonnepaneel modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZonnepaneelModelnaam",
                         definition="De modelnaam van het zonnepaneel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonnepaneelModelnaam")

