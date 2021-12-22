from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLaagRol(Keuzelijst):
    """De mogelijke rollen van de laag."""

    def __init__(self):
        super().__init__(naam="KlLaagRol",
                         label="Laag rol",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLaagRol",
                         definition="De mogelijke rollen van de laag.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLaagRol")

        self.add_option("wapening", "wapening", "De laag als wapening en/of bescherming.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/wapening")
        self.add_option("straatlaag", "straatlaag", "De laag als straatlaag", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/straatlaag")
        self.add_option("aanvulling", "aanvulling", "De laag als aanvulling.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/aanvulling")
        self.add_option("onderfundering", "onderfundering", "De laag als onderfundering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/onderfundering")
        self.add_option("verharding", "verharding", "De laag als verharding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/verharding")
        self.add_option("omhulling", "omhulling", "De laag als omhulling.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/omhulling")
        self.add_option("bed-van-bestrating", "bed van bestrating", "Dit betekent hetzelfde als 'straatlaag'. Gelieve voor deze optie 'straatlaag' aan te duiden als keuzemogelijkheid!", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/bed-van-bestrating")
        self.add_option("fundering", "fundering", "De laag als fundering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/fundering")
        self.add_option("fundering-voor-lijnvormige-elementen", "fundering voor lijnvormige elementen", "De laag als fundering voor lijnvormige elementen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/fundering-voor-lijnvormige-elementen")
