# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZenderMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Zender."""

    def __init__(self):
        super().__init__(naam="KlZenderMerk",
                         label="zender merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZenderMerk",
                         definition="Keuzelijst met merknamen voor Zender.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZenderMerk")

