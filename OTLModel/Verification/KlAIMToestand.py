from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField, Keuzelijst


class KlAIMToestand(Keuzelijst):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""

    def __init__(self):
        super().__init__(naam="KlAIMToestand", label="AIM toestand",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand",
                         definition="TKeuzelijst met fasen uit de levenscyclus van een object om de toestand op een "
                                    "moment mee vast te leggen.", usagenote="", deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand")
        self.add_option("in-ontwerp", "in ontwerp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept"
                                                        "/KlAIMToestand/in-ontwerp")
        self.add_option("gepland", "gepland", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand"
                                                  "/gepland")
        self.add_option("in-gebruik", "in gebruik", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept"
                                                        "/KlAIMToestand/in-gebruik")
