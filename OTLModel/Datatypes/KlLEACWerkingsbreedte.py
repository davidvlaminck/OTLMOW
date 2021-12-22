from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEACWerkingsbreedte(Keuzelijst):
    """De verschillende mogelijke werkingsbreedtes."""

    def __init__(self):
        super().__init__(naam="KlLEACWerkingsbreedte",
                         label="Werkingsbreedte",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACWerkingsbreedte",
                         definition="De verschillende mogelijke werkingsbreedtes.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACWerkingsbreedte")

        self.add_option("W1", "W1", "Wn<=0,6", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W1")
        self.add_option("W2", "W2", "Wn<=0,8", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W2")
        self.add_option("W3", "W3", "Wn<=1,0", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W3")
        self.add_option("W4", "W4", "Wn<=1,3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W4")
        self.add_option("W5", "W5", "Wn<=1,7", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W5")
        self.add_option("W6", "W6", "Wn<=2,1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W6")
        self.add_option("W7", "W7", "Wn<=2,5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W7")
        self.add_option("W8", "W8", "Wn<=3,5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W8")
