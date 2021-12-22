from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBoomConflicten(Keuzelijst):
    """De verschillende mogelijke conflicten van een boom."""

    def __init__(self):
        super().__init__(naam="KlBoomConflicten",
                         label="Boom conflicten",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConflicten",
                         definition="De verschillende mogelijke conflicten van een boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConflicten")

        self.add_option("hinderende-takken", "hinderende takken", "Takken die hinderlijk zijn voor de zichtbaarheid en de vrije doorrijhoogte of die luchtleidingen raken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/hinderende-takken")
        self.add_option("wortelopdruk", "wortelopdruk", "Boomwortels die (weg)verhardingselementen opdrukken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/wortelopdruk")
        self.add_option("verharding", "verharding", "Een verhardingslaag bevindt zich zeer dicht tegen de boom", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/verharding")
        self.add_option("bodemverdichting", "bodemverdichting", "Verdichting van de bodem door belasting (voetgangers, fietsers, auto's, bouwmaterialen,...)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/bodemverdichting")
        self.add_option("te-dicht-bij-rand-verharding", "te dicht bij rand verharding", "Verharding ligt op minder dan 50 cm van de stamvoet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/te-dicht-bij-rand-verharding")
        self.add_option("beperkte-doorwortelbare-ruimte", "beperkte doorwortelbare ruimte", "Het bodemvolume met voldoende mineralen, water en zuurstof waar de wortels van de boom zich kunnen ontwikkelen is veel lager dan verwacht", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/beperkte-doorwortelbare-ruimte")
        self.add_option("scheefstand", "scheefstand", "Schuin gezakte/gegroeide boom waarbij de top van de boom in het verlengde van de stam ligt en niet verticaal opgericht is", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/scheefstand")
        self.add_option("instabiel", "instabiel", "Een boom die niet stabiel in de grond staat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/instabiel")
        self.add_option("andere", "andere", "Andere mogelijke conflicten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/andere")
