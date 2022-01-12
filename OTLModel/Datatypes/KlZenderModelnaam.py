# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZenderModelnaam(Keuzelijst):
    """Keuzelijst met modelnamen voor Zender."""

    def __init__(self):
        super().__init__(naam="KlZenderModelnaam",
                         label="zender modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZenderModelnaam",
                         definition="Keuzelijst met modelnamen voor Zender.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZenderModelnaam")

