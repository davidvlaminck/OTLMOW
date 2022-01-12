# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcokokerType(Keuzelijst):
    """Types van ecokoker."""

    def __init__(self):
        super().__init__(naam="KlEcoEcokokerType",
                         label="Ecokoker type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcokokerType",
                         definition="Types van ecokoker.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcokokerType")

        self.add_option("amfibieenkoker", "amfibieenkoker", "Een ecokoker voor amfibieën.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/amfibieenkoker")
        self.add_option("betonnen-ecokoker", "betonnen ecokoker", "Een ecokoker uit beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/betonnen-ecokoker")
