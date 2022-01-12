# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuchtkwaliteitOpstellingModelnaam(Keuzelijst):
    """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""

    def __init__(self):
        super().__init__(naam="KlLuchtkwaliteitOpstellingModelnaam",
                         label="Luchtkwaliteitsopstelling modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLuchtkwaliteitOpstellingModelnaam",
                         definition="De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuchtkwaliteitOpstellingModelnaam")

        self.add_option("VICOTEC321", "VICOTEC321", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC321")
        self.add_option("VICOTEC322", "VICOTEC322", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC322")
        self.add_option("VICOTEC323", "VICOTEC323", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC323")
        self.add_option("VICOTEC324", "VICOTEC324", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC324")
