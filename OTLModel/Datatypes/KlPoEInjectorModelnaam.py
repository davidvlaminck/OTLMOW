# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPoEInjectorModelnaam(Keuzelijst):
    """De modelnaam van de PoE-injector."""

    def __init__(self):
        super().__init__(naam="KlPoEInjectorModelnaam",
                         label="Power over ethernet injector modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPoEInjectorModelnaam",
                         definition="De modelnaam van de PoE-injector.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoEInjectorModelnaam")

