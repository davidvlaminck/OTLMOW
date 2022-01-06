# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandhaspelMerk(Keuzelijst):
    """Het merk van de brandhaspel."""

    def __init__(self):
        super().__init__(naam="KlBrandhaspelMerk",
                         label="Brandhaspel merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandhaspelMerk",
                         definition="Het merk van de brandhaspel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandhaspelMerk")

