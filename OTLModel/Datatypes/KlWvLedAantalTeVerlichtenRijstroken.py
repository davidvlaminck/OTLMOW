from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWvLedAantalTeVerlichtenRijstroken(Keuzelijst):
    """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""

    def __init__(self):
        super().__init__(naam="KlWvLedAantalTeVerlichtenRijstroken",
                         label="WV LED aantal te verlichten rijstroken",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedAantalTeVerlichtenRijstroken",
                         definition="Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedAantalTeVerlichtenRijstroken")

        self.add_option("R1", "R1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R1")
        self.add_option("R2", "R2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R2")
        self.add_option("R3", "R3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R3")
        self.add_option("R4", "R4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R4")
        self.add_option("R5", "R5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R5")
        self.add_option("R6", "R6", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R6")
