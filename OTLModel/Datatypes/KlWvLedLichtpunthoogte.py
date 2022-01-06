# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedLichtpunthoogte(Keuzelijst):
    """Hoogte van het lichtpunt ten opzichte van de rijweg."""

    def __init__(self):
        super().__init__(naam="KlWvLedLichtpunthoogte",
                         label="WV LED lichtpunthoogte",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtpunthoogte",
                         definition="Hoogte van het lichtpunt ten opzichte van de rijweg.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedLichtpunthoogte")

        self.add_option("H20", "H20", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H20")
        self.add_option("H18", "H18", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H18")
        self.add_option("H16", "H16", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H16")
        self.add_option("H12", "H12", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H12")
        self.add_option("H10", "H10", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H10")
        self.add_option("H08", "H08", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H08")
        self.add_option("H06", "H06", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H06")
        self.add_option("H05", "H05", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H05")
        self.add_option("H04", "H04", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H04")
