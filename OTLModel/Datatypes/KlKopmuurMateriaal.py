# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKopmuurMateriaal(Keuzelijst):
    """Materialen van de kopmuur."""

    def __init__(self):
        super().__init__(naam="KlKopmuurMateriaal",
                         label="Kopmuur materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKopmuurMateriaal",
                         definition="Materialen van de kopmuur.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKopmuurMateriaal")

        self.add_option("beton", "beton", "beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKopmuurMateriaal/beton")
        self.add_option("metselwerk", "metselwerk", "metselwerk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKopmuurMateriaal/metselwerk")
