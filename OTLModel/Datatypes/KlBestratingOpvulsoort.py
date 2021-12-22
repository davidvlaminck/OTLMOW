from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBestratingOpvulsoort(Keuzelijst):
    """De mogelijke opvulsoorten van de grasbetontegel en graskunststofplaat."""

    def __init__(self):
        super().__init__(naam="KlBestratingOpvulsoort",
                         label="Bestrating opvulsoort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingOpvulsoort",
                         definition="De mogelijke opvulsoorten van de grasbetontegel en graskunststofplaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingOpvulsoort")

        self.add_option("bodemsubstraat", "bodemsubstraat", "Opgevuld met bodemsubstraat.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bodemsubstraat")
        self.add_option("bodemsubstraat-en-ingezaaid", "bodemsubstraat en ingezaaid", "Opgevuld met bodemsubstraat en ingezaaid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bodemsubstraat-en-ingezaaid")
        self.add_option("bomenzand", "bomenzand", "Opgevuld met bomenzand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bomenzand")
        self.add_option("bomenzand-en-ingezaaid", "bomenzand en ingezaaid", "Opgevuld met bomenzand en ingezaaid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bomenzand-en-ingezaaid")
        self.add_option("steenslag-2-6.3", "steenslag 2-6.3", "Opgevuld met steenslag 2/6,3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/steenslag-2-6.3")
