# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingstoestelSoortLamp(Keuzelijst):
    """Lijst van mogelijke soorten lampen voor binnenverlichtingstoestellen."""

    def __init__(self):
        super().__init__(naam="KlBinnenverlichtingstoestelSoortLamp",
                         label="Binnenverlichtingstoestel soort lamp",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSoortLamp",
                         definition="Lijst van mogelijke soorten lampen voor binnenverlichtingstoestellen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSoortLamp")

        self.add_option("LED", "LED", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/LED")
        self.add_option("TL", "TL", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/TL")
        self.add_option("gloeilamp", "gloeilamp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/gloeilamp")
        self.add_option("halogeen", "halogeen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/halogeen")
        self.add_option("spaarlamp", "spaarlamp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/spaarlamp")
