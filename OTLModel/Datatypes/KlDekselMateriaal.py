# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselMateriaal(Keuzelijst):
    """Het materiaal waaruit het deksel bestaat."""

    def __init__(self):
        super().__init__(naam="KlDekselMateriaal",
                         label="Dekselmateriaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselMateriaal",
                         definition="Het materiaal waaruit het deksel bestaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselMateriaal")

        self.add_option("cementmortel", "cementmortel", "cementmortel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/cementmortel")
        self.add_option("beton", "beton", "beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/beton")
        self.add_option("gewapend-beton", "gewapend beton", "gewapend beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/gewapend-beton")
        self.add_option("betonnen-segmenten", "betonnen segmenten", "betonnen segmenten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/betonnen-segmenten")
        self.add_option("gietijzer", "gietijzer", "nodulair gietijzer", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/gietijzer")
        self.add_option("grijs-gietijzer", "grijs gietijzer", "grijs gietijzer", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/grijs-gietijzer")
        self.add_option("smeedijzer", "smeedijzer", "smeedijzer", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/smeedijzer")
        self.add_option("staal", "staal", "staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/staal")
        self.add_option("ongeïdentificeerd-type-ijzer-of-staal", "ongeïdentificeerd type ijzer of staal", "ongeïdentificeerd type ijzer of staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeïdentificeerd-type-ijzer-of-staal")
        self.add_option("ongeïdentificeerd-type-kunststof", "ongeïdentificeerd type kunststof", "ongeïdentificeerd type kunststof", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeïdentificeerd-type-kunststof")
        self.add_option("ongeïdentificeerd-materiaal", "ongeïdentificeerd materiaal", "ongeïdentificeerd materiaal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeïdentificeerd-materiaal")
        self.add_option("anders", "anders", "anders", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/anders")
