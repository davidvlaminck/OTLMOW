# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerModelnaam(Keuzelijst):
    """De modelnaam van de virtuele server."""

    def __init__(self):
        super().__init__(naam="KlVirtueleServerModelnaam",
                         label="Virtuele server modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerModelnaam",
                         definition="De modelnaam van de virtuele server.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerModelnaam")

