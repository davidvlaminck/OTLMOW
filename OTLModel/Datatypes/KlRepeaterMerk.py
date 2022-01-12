# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRepeaterMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Repeater."""

    def __init__(self):
        super().__init__(naam="KlRepeaterMerk",
                         label="repeater merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRepeaterMerk",
                         definition="Keuzelijst met merknamen voor Repeater.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRepeaterMerk")

