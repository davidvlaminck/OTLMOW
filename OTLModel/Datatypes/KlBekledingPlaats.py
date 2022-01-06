# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBekledingPlaats(Keuzelijst):
    """Mogelijke locaties van de bekleding op de buis of put."""

    def __init__(self):
        super().__init__(naam="KlBekledingPlaats",
                         label="Bekleding plaats",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBekledingPlaats",
                         definition="Mogelijke locaties van de bekleding op de buis of put.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBekledingPlaats")

        self.add_option("inwendig", "inwendig", "binnenzijde van de buis/put, waar deze in contact staat met het medium dat door de buis/put wordt getransporteerd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBekledingPlaats/inwendig")
        self.add_option("uitwendig", "uitwendig", "buitenzijde van de buis/put, waar deze in contact staat met de omgeving", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBekledingPlaats/uitwendig")
