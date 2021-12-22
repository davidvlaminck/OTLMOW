from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVrStuurkaartCommunicatieprotocol(Keuzelijst):
    """Keuzelist met de voorkomende communicatieprotocollen voor VRIstuurkaarten."""

    def __init__(self):
        super().__init__(naam="KlVrStuurkaartCommunicatieprotocol",
                         label="VRI-communicatieprotocol",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVrStuurkaartCommunicatieprotocol",
                         definition="Keuzelist met de voorkomende communicatieprotocollen voor VRIstuurkaarten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVrStuurkaartCommunicatieprotocol")

        self.add_option("ocit", "ocit", "nog in te vullen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/ocit")
        self.add_option("canto", "canto", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/canto")
        self.add_option("gecombineerd", "gecombineerd", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/gecombineerd")
