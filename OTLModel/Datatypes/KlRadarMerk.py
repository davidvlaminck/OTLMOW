# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Radar."""

    def __init__(self):
        super().__init__(naam="KlRadarMerk",
                         label="Radar merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarMerk",
                         definition="Keuzelijst met merknamen voor Radar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarMerk")

