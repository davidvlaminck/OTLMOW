from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlPlaatsingswijzePlint(Keuzelijst):
    """De manier waarop de plint geplaatst is ten opzichte van de profielen."""

    def __init__(self):
        super().__init__(naam="KlPlaatsingswijzePlint",
                         label="Plaatsingswijze plint",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlaatsingswijzePlint",
                         definition="De manier waarop de plint geplaatst is ten opzichte van de profielen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingswijzePlint")

        self.add_option("bevestigd-tegen-de-profielen", "bevestigd tegen de profielen", "bevestigd tegen de profielen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijzePlint/bevestigd-tegen-de-profielen")
        self.add_option("geschoven-tussen-de-profielen", "geschoven tussen de profielen", "geschoven tussen de profielen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijzePlint/geschoven-tussen-de-profielen")
