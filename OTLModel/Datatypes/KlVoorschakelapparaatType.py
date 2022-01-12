# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoorschakelapparaatType(Keuzelijst):
    """Type van het voorschakelapparaat."""

    def __init__(self):
        super().__init__(naam="KlVoorschakelapparaatType",
                         label="Voorschakelapparaat type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoorschakelapparaatType",
                         definition="Type van het voorschakelapparaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoorschakelapparaatType")

        self.add_option("elektromechanisch", "elektromechanisch", "/ CLASS : IVSB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/elektromechanisch")
        self.add_option("elektronisch", "elektronisch", "/ CLASS : IVSB", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/elektronisch")
