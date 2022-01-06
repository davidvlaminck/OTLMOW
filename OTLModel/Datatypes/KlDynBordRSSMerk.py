# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRSSMerk(Keuzelijst):
    """Keuzelijst met de gangbare merken van RSS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordRSSMerk",
                         label="Dyn bord RSS merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRSSMerk",
                         definition="Keuzelijst met de gangbare merken van RSS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRSSMerk")

