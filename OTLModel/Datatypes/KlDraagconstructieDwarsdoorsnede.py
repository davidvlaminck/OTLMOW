from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDraagconstructieDwarsdoorsnede(Keuzelijst):
    """Lijst van mogelijke vormen van dwarsdoorsnedes van een draagconstructie."""

    def __init__(self):
        super().__init__(naam="KlDraagconstructieDwarsdoorsnede",
                         label="Draagconstructie dwarsdoorsnede",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagconstructieDwarsdoorsnede",
                         definition="Lijst van mogelijke vormen van dwarsdoorsnedes van een draagconstructie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagconstructieDwarsdoorsnede")

        self.add_option("rond", "rond", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/rond")
        self.add_option("vierkant", "vierkant", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/vierkant")
        self.add_option("octagonaal", "octagonaal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/octagonaal")
