# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPLCMerk(Keuzelijst):
    """Het merk van de PLC."""

    def __init__(self):
        super().__init__(naam="KlPLCMerk",
                         label="PLC merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPLCMerk",
                         definition="Het merk van de PLC.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPLCMerk")

