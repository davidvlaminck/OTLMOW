# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordOpMaatMerk(Keuzelijst):
    """Keuzelijst met de gangbare merken van dynamische borden op maat. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordOpMaatMerk",
                         label="Keuzelijst merknamen voor dynamische borden op maat",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordOpMaatMerk",
                         definition="Keuzelijst met de gangbare merken van dynamische borden op maat. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordOpMaatMerk")

