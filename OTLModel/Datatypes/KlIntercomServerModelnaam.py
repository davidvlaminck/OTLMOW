# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomServerModelnaam(Keuzelijst):
    """De modelnaam van de intercomserver."""

    def __init__(self):
        super().__init__(naam="KlIntercomServerModelnaam",
                         label="Intercomserver modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomServerModelnaam",
                         definition="De modelnaam van de intercomserver.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomServerModelnaam")

