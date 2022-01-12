# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHandbedieningType(Keuzelijst):
    """Types van handbediening voor toestellen bevestigd aan een kast."""

    def __init__(self):
        super().__init__(naam="KlHandbedieningType",
                         label="Handbediening type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHandbedieningType",
                         definition="Types van handbediening voor toestellen bevestigd aan een kast.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHandbedieningType")

        self.add_option("drukknop", "drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHandbedieningType/drukknop")
        self.add_option("schakelaar", "schakelaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHandbedieningType/schakelaar")
        self.add_option("sleutelcontact", "sleutelcontact", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHandbedieningType/sleutelcontact")
