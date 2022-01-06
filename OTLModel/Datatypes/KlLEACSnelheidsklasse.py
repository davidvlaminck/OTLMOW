# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACSnelheidsklasse(Keuzelijst):
    """De verschillende snelheidsklasses van afschermende constructies."""

    def __init__(self):
        super().__init__(naam="KlLEACSnelheidsklasse",
                         label="Snelheidsklasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSnelheidsklasse",
                         definition="De verschillende snelheidsklasses van afschermende constructies.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSnelheidsklasse")

        self.add_option("C60", "C60", "Getest bij 60 km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSnelheidsklasse/C60")
        self.add_option("C70", "C70", "Getest bij 70 km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSnelheidsklasse/C70")
