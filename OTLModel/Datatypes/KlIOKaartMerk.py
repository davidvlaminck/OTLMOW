# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOKaartMerk(Keuzelijst):
    """Lijst van mogelijke merken voor IO-kaarten."""

    def __init__(self):
        super().__init__(naam="KlIOKaartMerk",
                         label="IO-kaart merken",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOKaartMerk",
                         definition="Lijst van mogelijke merken voor IO-kaarten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOKaartMerk")

