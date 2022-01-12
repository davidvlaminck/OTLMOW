# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompModelnaam(Keuzelijst):
    """Lijst met modelnamen voor pompen."""

    def __init__(self):
        super().__init__(naam="KlPompModelnaam",
                         label="Typepomp modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPompModelnaam",
                         definition="Lijst met modelnamen voor pompen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompModelnaam")

