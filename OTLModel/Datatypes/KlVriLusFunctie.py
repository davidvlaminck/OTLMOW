# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusFunctie(Keuzelijst):
    """Keuzelijst met verschillende types detectielussen naar functie."""

    def __init__(self):
        super().__init__(naam="KlVriLusFunctie",
                         label="VRI-lus functie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusFunctie",
                         definition="Keuzelijst met verschillende types detectielussen naar functie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusFunctie")

        self.add_option("filelus", "filelus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/filelus")
        self.add_option("afstandslus", "afstandslus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/afstandslus")
        self.add_option("hiaatlus", "hiaatlus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/hiaatlus")
        self.add_option("KAR-inmeldlus", "KAR inmeldlus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-inmeldlus")
        self.add_option("KAR-uitmeldlus", "KAR uitmeldlus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-uitmeldlus")
        self.add_option("stopstreeplus", "stopstreeplus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/stopstreeplus")
