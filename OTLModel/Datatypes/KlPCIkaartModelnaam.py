# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPCIkaartModelnaam(Keuzelijst):
    """De modelnaam van de PCI-kaart."""

    def __init__(self):
        super().__init__(naam="KlPCIkaartModelnaam",
                         label="PCI-kaart modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPCIkaartModelnaam",
                         definition="De modelnaam van de PCI-kaart.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPCIkaartModelnaam")

