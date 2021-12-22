from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlSeinlantaarnDiameter(Keuzelijst):
    """Keuzelijst met de verschillende voorkomende diameter-waarden voor Seinlantaarn."""

    def __init__(self):
        super().__init__(naam="KlSeinlantaarnDiameter",
                         label="Seinlantaarn diameter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnDiameter",
                         definition="Keuzelijst met de verschillende voorkomende diameter-waarden voor Seinlantaarn.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnDiameter")

        self.add_option("100", "100", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/100")
        self.add_option("200", "200", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/200")
        self.add_option("300", "300", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/300")
