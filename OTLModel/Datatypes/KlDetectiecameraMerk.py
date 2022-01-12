# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Detectiecamera."""

    def __init__(self):
        super().__init__(naam="KlDetectiecameraMerk",
                         label="Detectiecamera merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraMerk",
                         definition="Keuzelijst met merknamen voor Detectiecamera.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraMerk")

