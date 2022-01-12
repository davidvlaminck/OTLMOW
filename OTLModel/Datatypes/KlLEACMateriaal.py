# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACMateriaal(Keuzelijst):
    """De verschillende materialen voor afschermende constructies."""

    def __init__(self):
        super().__init__(naam="KlLEACMateriaal",
                         label="Materiaal",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACMateriaal",
                         definition="De verschillende materialen voor afschermende constructies.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACMateriaal")

        self.add_option("geprefabriceerde-beton", "geprefabriceerde beton", "geleideconstructie bestaande uit geprefabriceerde betonnen elementen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/geprefabriceerde-beton")
        self.add_option("hout-staal", "hout-staal", "hout-staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/hout-staal")
        self.add_option("in-situ-beton", "in situ beton", "in situ beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/in-situ-beton")
        self.add_option("kunststof", "kunststof", "kunststof", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/kunststof")
        self.add_option("staal", "staal", "staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/staal")
