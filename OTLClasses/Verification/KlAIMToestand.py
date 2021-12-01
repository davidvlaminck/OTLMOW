from ModelGenerator.BaseClasses.Keuzelijst import Keuzelijst


class KlAIMToestand(Keuzelijst):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""
    def __init__(self):
        super(KlAIMToestand, self).__init__('KlAIMToestand', 'AIM toestand',
                                            "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand")
        self.addOption("in-ontwerp", "in ontwerp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp")
        self.addOption("gepland", "gepland", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/gepland")