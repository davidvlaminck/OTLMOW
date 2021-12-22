from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEDDriverProtocol(Keuzelijst):
    """Protocol gebruikt door de LED driver voor het aansturen van de LED's."""

    def __init__(self):
        super().__init__(naam="KlLEDDriverProtocol",
                         label="LED stuurprotocol",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverProtocol",
                         definition="Protocol gebruikt door de LED driver voor het aansturen van de LED's.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverProtocol")

        self.add_option("dali", "dali", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverProtocol/dali")
        self.add_option("daliv2", "daliv2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverProtocol/daliv2")
        self.add_option("1-10v", "1-10v", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverProtocol/1-10v")
