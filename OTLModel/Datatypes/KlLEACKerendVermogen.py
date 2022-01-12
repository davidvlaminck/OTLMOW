# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACKerendVermogen(Keuzelijst):
    """De verschillende niveaus van kerend vermogen gedefinieerd : van T1 (laagste niveau) tot H4b (hoogste niveau)  Voor elk kerend vermogen wordt in de norm precies vastgelegd welke botsproeven moeten uitgevoerd worden."""

    def __init__(self):
        super().__init__(naam="KlLEACKerendVermogen",
                         label="Kerend vermogen",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACKerendVermogen",
                         definition="De verschillende niveaus van kerend vermogen gedefinieerd : van T1 (laagste niveau) tot H4b (hoogste niveau)  Voor elk kerend vermogen wordt in de norm precies vastgelegd welke botsproeven moeten uitgevoerd worden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACKerendVermogen")

        self.add_option("H1", "H1", "hoog kerend vermogen, getest met een vrachtwagen van 10 ton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H1")
        self.add_option("H2", "H2", "hoog kerend vermogen, getest met een bus van 13 ton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H2")
        self.add_option("H3", "H3", "hoog kerend vermogen, getest met een vrachtwagen van 16 ton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H3")
        self.add_option("H4a", "H4a", "zeer hoog kerend vermogen, getest met een vrachtwagen van 30 ton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H4a")
        self.add_option("H4b", "H4b", "zeer hoog kerend vermogen, getest met een vrachtwagen van 38 ton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H4b")
        self.add_option("N1", "N1", "normaal kerend vermogen, getest met een wagen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/N1")
        self.add_option("N2", "N2", "normaal kerend vermogen, getest met een wagen aan hoge snelheid", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/N2")
        self.add_option("T1", "T1", "kerend vermogen voor lage impacthoeken, geschikt voor tijdelijke situaties, getest met een wagen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/T1")
        self.add_option("T2", "T2", "kerend vermogen voor lage impacthoeken, geschikt voor tijdelijke situaties, getest met een wagen maar voor hogere impacthoeken dan T1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/T2")
        self.add_option("T3", "T3", "kerend vermogen voor lage impacthoeken, geschikt voor tijdelijke situaties, getest met een vrachtwagen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/T3")
