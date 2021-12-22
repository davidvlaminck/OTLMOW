from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlTerugslagklepType(Keuzelijst):
    """Keuzelijst voor het bepalen van Types van terugslagklep."""

    def __init__(self):
        super().__init__(naam="KlTerugslagklepType",
                         label="Terugslagklep type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTerugslagklepType",
                         definition="Keuzelijst voor het bepalen van Types van terugslagklep.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTerugslagklepType")

        self.add_option("vorm-eendebek", "vorm eendebek", "Eendebek, bedoeld om terugstroom in het stelsel vanuit het oppervlaktewater te voorkomen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTerugslagklepType/vorm-eendebek")
        self.add_option("scharnierend", "scharnierend", "Klep bevestigd aan een scharnier, bedoeld om terugstroom in het stelsel vanuit het oppervlaktewater te voorkomen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTerugslagklepType/scharnierend")
        self.add_option("balkeerklep", "balkeerklep", "balkeerklep", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTerugslagklepType/balkeerklep")
