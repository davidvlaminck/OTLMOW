# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKMerk(Keuzelijst):
    """Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordPKMerk",
                         label="Dyn bord PK merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKMerk",
                         definition="Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKMerk")

