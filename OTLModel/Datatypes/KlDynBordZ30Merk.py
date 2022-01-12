# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordZ30Merk(Keuzelijst):
    """Keuzelijst met de gangbare merken van dynamische zone 30 borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordZ30Merk",
                         label="Z30 merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordZ30Merk",
                         definition="Keuzelijst met de gangbare merken van dynamische zone 30 borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordZ30Merk")

        self.add_option("Futurit", "Futurit", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Merk/Futurit")
        self.add_option("Q-lite", "Q-lite", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Merk/Q-lite")
