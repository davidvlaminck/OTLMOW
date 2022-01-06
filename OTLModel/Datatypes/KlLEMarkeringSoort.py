# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEMarkeringSoort(Keuzelijst):
    """Mogelijke markeringsoorten op een lijvormig element."""

    def __init__(self):
        super().__init__(naam="KlLEMarkeringSoort",
                         label="Soort markering van lijnvormig element",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEMarkeringSoort",
                         definition="Mogelijke markeringsoorten op een lijvormig element.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEMarkeringSoort")

        self.add_option("new-Jersey", "new Jersey", "Een afschermende constructie uit kunststof, beton of metaal dat naast wegen wordt geplaatst om te voorkomen dat voertuigen de weg in zijdelingse richting verlaten, kantelen of de middenberm doorkruisen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/new-Jersey")
        self.add_option("boordsteen", "boordsteen", "Een lijnvormig element dat de scheiding verzorgt tussen een rijbaan en het meestal hoger gelegen trottoir", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/boordsteen")
        self.add_option("boordsteen-parkeerverbod", "boordsteen parkeerverbod", "Een lijnvormig element dat de scheiding verzorgt tussen een rijbaan en het meestal hoger gelegen trottoir met als functie het aanduiden van parkeerverbod", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/boordsteen-parkeerverbod")
        self.add_option("vangrail", "vangrail", "Een afschermende constructie die naast wegen wordt geplaatst om te voorkomen dat voertuigen de weg in zijdelingse richting verlaten, kantelen of de middenberm doorkruisen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/vangrail")
        self.add_option("biggenrug", "biggenrug", "Een betonnen obstakel dat meestal een infrastructurele en beschermende functie heeft", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/biggenrug")
