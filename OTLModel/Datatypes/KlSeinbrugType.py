# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugType(Keuzelijst):
    """Types van seinbrug."""

    def __init__(self):
        super().__init__(naam="KlSeinbrugType",
                         label="Seinbrug type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugType",
                         definition="Types van seinbrug.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugType")

        self.add_option("koker", "koker", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/koker")
        self.add_option("nietDoorlopendeBuis", "nietDoorlopendeBuis", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/nietDoorlopendeBuis")
        self.add_option("vakwerk", "vakwerk", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/vakwerk")
        self.add_option("enkeleLigger", "enkeleLigger", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/enkeleLigger")
