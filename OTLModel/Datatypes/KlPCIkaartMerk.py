# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPCIkaartMerk(Keuzelijst):
    """Het merk van de PCI-kaart."""

    def __init__(self):
        super().__init__(naam="KlPCIkaartMerk",
                         label="PCI-kaart merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPCIkaartMerk",
                         definition="Het merk van de PCI-kaart.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPCIkaartMerk")

