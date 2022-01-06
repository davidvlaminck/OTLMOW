# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineModelnaam(Keuzelijst):
    """Modelnamen voor cabines."""

    def __init__(self):
        super().__init__(naam="KlCabineModelnaam",
                         label="Cabine modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineModelnaam",
                         definition="Modelnamen voor cabines.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineModelnaam")

