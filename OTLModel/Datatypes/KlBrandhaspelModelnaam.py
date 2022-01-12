# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandhaspelModelnaam(Keuzelijst):
    """De modelnaam van de brandhaspel."""

    def __init__(self):
        super().__init__(naam="KlBrandhaspelModelnaam",
                         label="brandhaspel model naam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandhaspelModelnaam",
                         definition="De modelnaam van de brandhaspel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandhaspelModelnaam")

