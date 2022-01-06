# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCodeklavierMerk(Keuzelijst):
    """Het merk van het codeklavier."""

    def __init__(self):
        super().__init__(naam="KlCodeklavierMerk",
                         label="Codeklavier merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCodeklavierMerk",
                         definition="Het merk van het codeklavier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCodeklavierMerk")

