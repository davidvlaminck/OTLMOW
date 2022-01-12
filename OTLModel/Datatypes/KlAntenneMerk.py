# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Antenne."""

    def __init__(self):
        super().__init__(naam="KlAntenneMerk",
                         label="Antenne merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneMerk",
                         definition="Keuzelijst met merknamen voor Antenne.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneMerk")

