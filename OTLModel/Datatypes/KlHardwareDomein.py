from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHardwareDomein(Keuzelijst):
    """Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""

    def __init__(self):
        super().__init__(naam="KlHardwareDomein",
                         label="Hardware domein",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareDomein",
                         definition="Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareDomein")

        self.add_option("belfla", "belfla", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/belfla")
        self.add_option("alfa", "alfa", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/alfa")
