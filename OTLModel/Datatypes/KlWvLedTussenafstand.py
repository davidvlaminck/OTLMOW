from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWvLedTussenafstand(Keuzelijst):
    """Afstand tussen de verschillende LED verlichtingstoestellen."""

    def __init__(self):
        super().__init__(naam="KlWvLedTussenafstand",
                         label="WV LED tussenafstand",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedTussenafstand",
                         definition="Afstand tussen de verschillende LED verlichtingstoestellen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedTussenafstand")

        self.add_option("S100", "S100", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S100")
        self.add_option("S090", "S090", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S090")
        self.add_option("S080", "S080", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S080")
        self.add_option("S070", "S070", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S070")
        self.add_option("S060", "S060", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S060")
        self.add_option("S050", "S050", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S050")
        self.add_option("S045", "S045", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S045")
        self.add_option("S040", "S040", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S040")
        self.add_option("S035", "S035", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S035")
        self.add_option("S030", "S030", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S030")
        self.add_option("S025", "S025", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S025")
        self.add_option("S020", "S020", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S020")
        self.add_option("S015", "S015", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S015")
