# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomModelnaam(Keuzelijst):
    """De modelnaam van het intercomtoestel."""

    def __init__(self):
        super().__init__(naam="KlIntercomModelnaam",
                         label="intercomtoestel modelnamen",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomModelnaam",
                         definition="De modelnaam van het intercomtoestel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomModelnaam")

