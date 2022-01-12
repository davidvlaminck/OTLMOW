# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAIDModuleType(Keuzelijst):
    """Het type van de AID-module."""

    def __init__(self):
        super().__init__(naam="KlAIDModuleType",
                         label="AID-module type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAIDModuleType",
                         definition="Het type van de AID-module.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIDModuleType")

