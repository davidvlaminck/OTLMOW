from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBoogpaalType(Keuzelijst):
    """Draagwijdte van de boogpaal."""

    def __init__(self):
        super().__init__(naam="KlBoogpaalType",
                         label="Type boogpaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoogpaalType",
                         definition="Draagwijdte van de boogpaal.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoogpaalType")

        self.add_option("3.50", "3.50", "middelgrote draagwijdte", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoogpaalType/3.50")
        self.add_option("7.50", "7.50", "grote draagwijdte", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoogpaalType/7.50")
