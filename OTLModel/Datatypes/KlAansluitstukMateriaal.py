# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitstukMateriaal(Keuzelijst):
    """Het materiaal van het aansluitstuk."""

    def __init__(self):
        super().__init__(naam="KlAansluitstukMateriaal",
                         label="Aansluitstuk materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitstukMateriaal",
                         definition="Het materiaal van het aansluitstuk.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitstukMateriaal")

        self.add_option("gres", "gres", "Gres", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/gres")
        self.add_option("polyethyleen", "polyethyleen", "polyethyleen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/polyethyleen")
        self.add_option("pvc", "pvc", "Polyvinylchloride", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pvc")
        self.add_option("pvc-u-composiet", "pvc-u-composiet", "pvc-u-composiet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pvc-u-composiet")
        self.add_option("pp", "pp", "Polypropyleen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pp")
