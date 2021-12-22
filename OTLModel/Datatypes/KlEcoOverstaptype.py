from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlEcoOverstaptype(Keuzelijst):
    """Types van terugkeer voor wild."""

    def __init__(self):
        super().__init__(naam="KlEcoOverstaptype",
                         label="Overstaptype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoOverstaptype",
                         definition="Types van terugkeer voor wild.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoOverstaptype")

        self.add_option("dassenpoort", "dassenpoort", "Een dassenpoortje is een luikje dat schuin in het raster bevestigd is. Dat luikje gaat maar langs één kant open en valt automatisch terug dicht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoOverstaptype/dassenpoort")
        self.add_option("ree-overstap", "ree overstap", "Een verhoging aan de buitenzijde (aan de kant van de weg) met een steile afsprong naar de binnenzijde om dieren die toch aan de wegkant verzeild zijn geraakt terug naar de veilige kant te laten begeven. Door de steile afsprong kan het dier niet in de richting van de weg gaan.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoOverstaptype/ree-overstap")
