from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField


class KlAlgGemeente(KeuzelijstField):
    """Lijst van gemeentes in Vlaanderen."""

    def __init__(self, optionByLabel: str = None):
        super().__init__(
            naam="KlAlgGemeente", label="Gemeente",
            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente",
            definition="Lijst van gemeentes in Vlaanderen.", constraints="", usagenote="", deprecated_version="",
            codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgGemeente")
        self.add_option("aalst", "aalst", "",
                        "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgGemeente/aalst")
        self.add_option("de-Haan", "de Haan", "",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgGemeente/de-Haan")

        self.set_value_by_label_on_init(optionByLabel)
