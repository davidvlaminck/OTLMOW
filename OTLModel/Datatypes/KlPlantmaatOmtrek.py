# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlantmaatOmtrek(Keuzelijst):
    """De stamomtrek in centimeter (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""

    def __init__(self):
        super().__init__(naam="KlPlantmaatOmtrek",
                         label="Plantmaat omtrek",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlantmaatOmtrek",
                         definition="De stamomtrek in centimeter (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantmaatOmtrek")

        self.add_option("6-8", "6/8", "Houtige vegetatie met stamomtrek tussen 6 en 8 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/6-8")
        self.add_option("8-10", "8/10", "Houtige vegetatie met stamomtrek tussen 8 en 10 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/8-10")
        self.add_option("10-12", "10/12", "Houtige vegetatie met stamomtrek tussen 10 en 12 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/10-12")
        self.add_option("12-14", "12/14", "Houtige vegetatie met stamomtrek tussen 12 en 14 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/12-14")
        self.add_option("14-16", "14/16", "Houtige vegetatie met stamomtrek tussen 14 en 16 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/14-16")
        self.add_option("16-18", "16/18", "Houtige vegetatie met stamomtrek tussen 16 en 18 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/16-18")
        self.add_option("18-20", "18/20", "Houtige vegetatie met stamomtrek tussen 18 en 20 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/18-20")
        self.add_option("20-25", "20/25", "Houtige vegetatie met stamomtrek tussen 20 en 25 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/20-25")
        self.add_option("25-30", "25/30", "Houtige vegetatie met stamomtrek tussen 25 en 30 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/25-30")
        self.add_option("30-40", "30/40", "Houtige vegetatie met stamomtrek tussen 30 en 40 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/30-40")
        self.add_option("30-35", "30/35", "Houtige vegetatie met stamomtrek tussen 30 en 35 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/30-35")
        self.add_option("35-40", "35/40", "Houtige vegetatie met stamomtrek tussen 35 en 40 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/35-40")
        self.add_option("40-50", "40/50", "Houtige vegetatie met stamomtrek tussen 40 en 50 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/40-50")
        self.add_option("50-60", "50/60", "Houtige vegetatie met stamomtrek tussen 50 en 60 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatOmtrek/50-60")
