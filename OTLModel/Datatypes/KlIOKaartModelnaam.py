# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOKaartModelnaam(Keuzelijst):
    """Lijst van mogelijke modelnamen voor IO-kaarten."""

    def __init__(self):
        super().__init__(naam="KlIOKaartModelnaam",
                         label="IO-kaart modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOKaartModelnaam",
                         definition="Lijst van mogelijke modelnamen voor IO-kaarten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOKaartModelnaam")

