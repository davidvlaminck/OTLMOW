# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomStandplaatswaarde(Keuzelijst):
    """De verschillende opties van de standplaatswaarde voor een boom."""

    def __init__(self):
        super().__init__(naam="KlBoomStandplaatswaarde",
                         label="Boom standplaatswaarde",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomStandplaatswaarde",
                         definition="De verschillende opties van de standplaatswaarde voor een boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomStandplaatswaarde")

        self.add_option("0.6", "0.6", "Landelijk gebied", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.6")
        self.add_option("0.7", "0.7", "Overgangszone: bebouwde kom - landelijk gebied", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.7")
        self.add_option("0.8", "0.8", "Open en halfopen bebouwing", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.8")
        self.add_option("0.9", "0.9", "Gesloten bebouwing", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.9")
        self.add_option("1.0", "1.0", "Sterk verstedelijkte stads- of dorpskern", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/1.0")
