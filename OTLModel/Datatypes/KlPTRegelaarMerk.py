# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarMerk(Keuzelijst):
    """Keuzelijst met merknamen voor PTRegelaar."""

    def __init__(self):
        super().__init__(naam="KlPTRegelaarMerk",
                         label="PT regelaar merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPTRegelaarMerk",
                         definition="Keuzelijst met merknamen voor PTRegelaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarMerk")

