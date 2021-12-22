from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEACPerformantieklasse(Keuzelijst):
    """De verschillende performantieklasses van de geteste beginconstructie."""

    def __init__(self):
        super().__init__(naam="KlLEACPerformantieklasse",
                         label="Performantieklasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACPerformantieklasse",
                         definition="De verschillende performantieklasses van de geteste beginconstructie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACPerformantieklasse")

        self.add_option("P1", "P1", "Beginconstructie enkel frontaal getest met een lichte wagen aan 80km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P1")
        self.add_option("P2", "P2", "Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 80km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P2")
        self.add_option("P3", "P3", "Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 100km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P3")
        self.add_option("P4", "P4", "Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en grote gezinswagen aan 110km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P4")
