# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUPSMerk(Keuzelijst):
    """Het merk van de UPS."""

    def __init__(self):
        super().__init__(naam="KlUPSMerk",
                         label="UPS merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUPSMerk",
                         definition="Het merk van de UPS.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUPSMerk")

