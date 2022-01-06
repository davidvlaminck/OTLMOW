# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOBitSnelheid(Keuzelijst):
    """Lijst met mogelijke bitsnelheden voor een invoer-uitvoer kaart of module."""

    def __init__(self):
        super().__init__(naam="KlIOBitSnelheid",
                         label="IO bit snelheid",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOBitSnelheid",
                         definition="Lijst met mogelijke bitsnelheden voor een invoer-uitvoer kaart of module.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOBitSnelheid")

        self.add_option("2", "2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/2")
        self.add_option("4", "4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/4")
        self.add_option("8", "8", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/8")
        self.add_option("16", "16", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/16")
        self.add_option("32", "32", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/32")
