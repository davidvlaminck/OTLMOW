# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijModelnaam(Keuzelijst):
    """De modelnaam van de batterij."""

    def __init__(self):
        super().__init__(naam="KlBatterijModelnaam",
                         label="Batterij modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijModelnaam",
                         definition="De modelnaam van de batterij.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijModelnaam")

