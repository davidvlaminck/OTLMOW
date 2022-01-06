# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerMerk(Keuzelijst):
    """Het merk van de virtuele server."""

    def __init__(self):
        super().__init__(naam="KlVirtueleServerMerk",
                         label="Virtuele server merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerMerk",
                         definition="Het merk van de virtuele server.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerMerk")

