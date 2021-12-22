from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBinnenverlichtingstoestelSchakelwijze(Keuzelijst):
    """Lijst met schakelwijzen voor een binnenverlichtingstoestel."""

    def __init__(self):
        super().__init__(naam="KlBinnenverlichtingstoestelSchakelwijze",
                         label="Binnenverlichtingstoestel schakelwijze",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSchakelwijze",
                         definition="Lijst met schakelwijzen voor een binnenverlichtingstoestel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSchakelwijze")

        self.add_option("timer", "timer", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/timer")
        self.add_option("schakelaar", "schakelaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/schakelaar")
        self.add_option("continu", "continu", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/continu")
