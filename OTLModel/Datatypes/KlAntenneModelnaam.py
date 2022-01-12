# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneModelnaam(Keuzelijst):
    """Keuzelijst met modelnamen voor Antenne."""

    def __init__(self):
        super().__init__(naam="KlAntenneModelnaam",
                         label="Antenne modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneModelnaam",
                         definition="Keuzelijst met modelnamen voor Antenne.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneModelnaam")

