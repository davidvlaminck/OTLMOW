# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAIMToestand(Keuzelijst):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""

    def __init__(self):
        super().__init__(naam="KlAIMToestand",
                         label="AIM toestand",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand",
                         definition="Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand")

        self.add_option("geannuleerd", "geannuleerd", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/geannuleerd")
        self.add_option("gepland", "gepland", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/gepland")
        self.add_option("in-gebruik", "in gebruik", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik")
        self.add_option("in-ontwerp", "in ontwerp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp")
        self.add_option("in-opbouw", "in opbouw", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw")
        self.add_option("overgedragen", "overgedragen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen")
        self.add_option("uit-gebruik", "uit gebruik", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/uit-gebruik")
        self.add_option("verwijderd", "verwijderd", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd")
