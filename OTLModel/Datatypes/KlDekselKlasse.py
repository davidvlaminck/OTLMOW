from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDekselKlasse(Keuzelijst):
    """Klassen van het deksel van de bovenbouw."""

    def __init__(self):
        super().__init__(naam="KlDekselKlasse",
                         label="Dekselklasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselKlasse",
                         definition="Klassen van het deksel van de bovenbouw.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselKlasse")

        self.add_option("C250-(voetpad)", "C250 (voetpad)", "C250 (voetpad)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/C250-(voetpad)")
        self.add_option("D400-(rijweg)", "D400 (rijweg)", "D400 (rijweg)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/D400-(rijweg)")
        self.add_option("E600-(rijweg-voor-zwaar-verkeer)", "E600 (rijweg voor zwaar verkeer)", "E600 (rijweg voor zwaar verkeer)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/E600-(rijweg-voor-zwaar-verkeer)")
        self.add_option("F900-(vliegvelden)", "F900 (vliegvelden)", "F900 (vliegvelden)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/F900-(vliegvelden)")
