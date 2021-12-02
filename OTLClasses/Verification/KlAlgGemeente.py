from ModelGenerator.BaseClasses.Keuzelijst import Keuzelijst


class KlAlgGemeente(Keuzelijst):
    """Lijst van gemeentes in Vlaanderen."""
    def __init__(self):
        super(KlAlgGemeente, self).__init__('KlAlgGemeente', 'Gemeente',
                                            "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgGemeente")
        self.addOption("aalst", "aalst", "", "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgGemeente/aalst")
        self.addOption("de-Haan", "de Haan", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgGemeente/de-Haan")