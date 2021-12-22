from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWegkantkastType(Keuzelijst):
    """Keuzelijst voor gangbare types voor wegkantkasten."""

    def __init__(self):
        super().__init__(naam="KlWegkantkastType",
                         label="Wegkantkast type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegkantkastType",
                         definition="Keuzelijst voor gangbare types voor wegkantkasten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegkantkastType")

        self.add_option("F", "F", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/F")
        self.add_option("E", "E", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/E")
        self.add_option("D", "D", "Wegkantkast type D", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/D")
        self.add_option("A", "A", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/A")
        self.add_option("DD", "DD", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/DD")
