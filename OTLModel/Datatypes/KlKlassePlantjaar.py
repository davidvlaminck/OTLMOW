# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlassePlantjaar(Keuzelijst):
    """Het geschatte tijdsinterval waarin de boom is aangeplant."""

    def __init__(self):
        super().__init__(naam="KlKlassePlantjaar",
                         label="Klasse plantjaar",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlassePlantjaar",
                         definition="Het geschatte tijdsinterval waarin de boom is aangeplant.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlassePlantjaar")

        self.add_option("1880-1900", "1880-1900", "De boom is aangeplant tussen 1880 en 1900.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1880-1900")
        self.add_option("1900-1920", "1900-1920", "De boom is aangeplant tussen 1900 en 1920.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1900-1920")
        self.add_option("1920-1940", "1920-1940", "De boom is aangeplant tussen 1920 en 1940.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1920-1940")
        self.add_option("1940-1960", "1940-1960", "De boom is aangeplant tussen 1940 en 1960.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1940-1960")
        self.add_option("1960-1980", "1960-1980", "De boom is aangeplant tussen 1960 en 1980.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1960-1980")
        self.add_option("1980-2000", "1980-2000", "De boom is aangeplant tussen 1980 en 2000.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1980-2000")
        self.add_option("2000-2020", "2000-2020", "De boom is aangeplant tussen 2000 en 2020.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/2000-2020")
        self.add_option("2020-2040", "2020-2040", "De boom is aangeplant tussen 2020 en 2040.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/2020-2040")
        self.add_option("ongekend", "ongekend", "Het is niet gekend wanneer de boom is aangeplant.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/ongekend")
