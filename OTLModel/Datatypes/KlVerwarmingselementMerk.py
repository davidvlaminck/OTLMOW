# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerwarmingselementMerk(Keuzelijst):
    """Keuzelijst van merken voor verwarmingselementen."""

    def __init__(self):
        super().__init__(naam="KlVerwarmingselementMerk",
                         label="Verwarmingselement merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerwarmingselementMerk",
                         definition="Keuzelijst van merken voor verwarmingselementen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerwarmingselementMerk")

