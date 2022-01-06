# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelMerk(Keuzelijst):
    """Het merk van de HS-beveiligingscel."""

    def __init__(self):
        super().__init__(naam="KlHSBeveiligingscelMerk",
                         label="HS-beveiligingscel merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelMerk",
                         definition="Het merk van de HS-beveiligingscel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelMerk")

