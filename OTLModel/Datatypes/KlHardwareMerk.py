# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareMerk(Keuzelijst):
    """Het merk van de hardware."""

    def __init__(self):
        super().__init__(naam="KlHardwareMerk",
                         label="Hardware merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareMerk",
                         definition="Het merk van de hardware.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareMerk")

