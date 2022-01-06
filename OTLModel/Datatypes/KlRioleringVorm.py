# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringVorm(Keuzelijst):
    """Vormen van de riolering."""

    def __init__(self):
        super().__init__(naam="KlRioleringVorm",
                         label="Riolering vorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringVorm",
                         definition="Vormen van de riolering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringVorm")

        self.add_option("rechthoekig", "rechthoekig", "Rechthoekig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/rechthoekig")
        self.add_option("cirkelvormig", "cirkelvormig", "Cirkelvormig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/cirkelvormig")
        self.add_option("andere", "andere", "Andere", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/andere")
        self.add_option("driehoekig", "driehoekig", "Driehoekig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/driehoekig")
        self.add_option("ovaal", "ovaal", "Ovaal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/ovaal")
        self.add_option("zeshoekig", "zeshoekig", "Zeshoekig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/zeshoekig")
        self.add_option("achthoekig", "achthoekig", "Achthoekig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/achthoekig")
        self.add_option("eivormig", "eivormig", "Eivormig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/eivormig")
        self.add_option("u-vorm", "u-vorm", "U-vorm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/u-vorm")
        self.add_option("gewelf", "gewelf", "Gewelf", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/gewelf")
        self.add_option("cunette", "cunette", "Cunette", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/cunette")
        self.add_option("vierkant", "vierkant", "Vierkant", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/vierkant")
