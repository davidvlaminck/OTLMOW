# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastArmlengte(Keuzelijst):
    """Lengte van de arm van de lichtmast in meter."""

    def __init__(self):
        super().__init__(naam="KlWvLichtmastArmlengte",
                         label="WV-mast armlengte",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastArmlengte",
                         definition="Lengte van de arm van de lichtmast in meter.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastArmlengte")

        self.add_option("1.5", "1.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/1.5")
        self.add_option("2", "2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/2")
        self.add_option("2.5", "2.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/2.5")
        self.add_option("3.2", "3.2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/3.2")
        self.add_option("niet-van-toepassing", "niet van toepassing", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/niet-van-toepassing")
