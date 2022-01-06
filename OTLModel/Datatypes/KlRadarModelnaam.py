# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarModelnaam(Keuzelijst):
    """Keuzelijst met modelnamen voor Radar."""

    def __init__(self):
        super().__init__(naam="KlRadarModelnaam",
                         label="Radar modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarModelnaam",
                         definition="Keuzelijst met modelnamen voor Radar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarModelnaam")

