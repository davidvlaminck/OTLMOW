# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDamwandMateriaal(Keuzelijst):
    """Het materiaal waaruit de damwand bestaat."""

    def __init__(self):
        super().__init__(naam="KlDamwandMateriaal",
                         label="Damwand materiaal",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDamwandMateriaal",
                         definition="Het materiaal waaruit de damwand bestaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDamwandMateriaal")

        self.add_option("beton", "beton", "beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDamwandMateriaal/beton")
        self.add_option("hout", "hout", "hout", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDamwandMateriaal/hout")
        self.add_option("staal", "staal", "staal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDamwandMateriaal/staal")
