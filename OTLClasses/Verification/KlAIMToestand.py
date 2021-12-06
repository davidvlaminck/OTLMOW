from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField


class KlAIMToestand(KeuzelijstField):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""

    def __init__(self, optionByLabel: str = None):
        super(KlAIMToestand, self).__init__('KlAIMToestand', 'AIM toestand',
                                            "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand")
        self.add_option("in-ontwerp", "in ontwerp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept"
                                                        "/KlAIMToestand/in-ontwerp")
        self.add_option("gepland", "gepland", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand"
                                                  "/gepland")

        self.set_value_by_label_on_init(optionByLabel)
