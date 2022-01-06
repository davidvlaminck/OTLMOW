# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringsbuisFunctie(Keuzelijst):
    """Mogelijke functies van de riolering."""

    def __init__(self):
        super().__init__(naam="KlRioleringsbuisFunctie",
                         label="Rioleringsbuis functie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringsbuisFunctie",
                         definition="Mogelijke functies van de riolering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringsbuisFunctie")

        self.add_option("syphon", "syphon", "buis bedoeld voor gravitaire afvoer van water met omgekeerde hevelwerking", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/syphon")
        self.add_option("infiltratieleiding", "infiltratieleiding", "buis bedoeld voor gravitaire afvoer en infiltratie van niet vervuild water", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/infiltratieleiding")
        self.add_option("bufferleiding", "bufferleiding", "buis bedoeld voor gravitaire afvoer en tijdelijke buffering van water", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/bufferleiding")
        self.add_option("gravitaire-leiding", "gravitaire leiding", "buis bedoeld voor de gravitaire afvoer van water", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/gravitaire-leiding")
