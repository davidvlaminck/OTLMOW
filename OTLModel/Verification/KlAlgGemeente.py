from OTLModel.Datatypes.KeuzelijstField import Keuzelijst


class KlAlgGemeente(Keuzelijst):
    """Lijst van gemeentes in Vlaanderen."""

    def __init__(self):
        super().__init__(naam="KlAlgGemeente",
                         label="Gemeente",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente",
                         definition="Lijst van gemeentes in Vlaanderen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgGemeente")

        self.add_option("aalst", "aalst", "", "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgGemeente/aalst")
        self.add_option("de-Haan", "de Haan", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgGemeente/de-Haan")
