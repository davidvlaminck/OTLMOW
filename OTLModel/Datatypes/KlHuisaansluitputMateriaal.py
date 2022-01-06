# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHuisaansluitputMateriaal(Keuzelijst):
    """Materialen voor een huisaansluitput."""

    def __init__(self):
        super().__init__(naam="KlHuisaansluitputMateriaal",
                         label="Huisaansluitput materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHuisaansluitputMateriaal",
                         definition="Materialen voor een huisaansluitput.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHuisaansluitputMateriaal")

        self.add_option("beton", "beton", "betonnen huisaansluitputje", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/beton")
        self.add_option("kunststof", "kunststof", "kunstof aansluitputje", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/kunststof")
        self.add_option("gres", "gres", "aansluitputje in grès", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/gres")
