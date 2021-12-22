from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlMaaiFrequentie(Keuzelijst):
    """Het aantal keer dat er gemaaid wordt per jaar."""

    def __init__(self):
        super().__init__(naam="KlMaaiFrequentie",
                         label="Maaifrequentie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiFrequentie",
                         definition="Het aantal keer dat er gemaaid wordt per jaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiFrequentie")

        self.add_option("1-3", "1/3", "Eén keer om de drie jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-3")
        self.add_option("1-2", "1/2", "Eén keer om de twee jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-2")
        self.add_option("1", "1", "Eén keer per jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1")
        self.add_option("2", "2", "Twee keer per jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/2")
        self.add_option("3", "3", "Drie keer per jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/3")
        self.add_option("4-6", "4-6", "Vier tot zes keer per jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/4-6")
        self.add_option("7-9", "7-9", "Zeven tot negen keer per jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/7-9")
        self.add_option("10-15", "10-15", "10 tot 15 keer per jaar maaien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/10-15")
