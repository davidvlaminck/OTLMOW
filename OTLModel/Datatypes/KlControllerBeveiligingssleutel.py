# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlControllerBeveiligingssleutel(Keuzelijst):
    """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""

    def __init__(self):
        super().__init__(naam="KlControllerBeveiligingssleutel",
                         label="Controller beveiligingssleutel.",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlControllerBeveiligingssleutel",
                         definition="De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlControllerBeveiligingssleutel")

        self.add_option("AES-256", "AES-256", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlControllerBeveiligingssleutel/AES-256")
