# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserBlusmiddel(Keuzelijst):
    """Keuzelijst met de verschillende mogelijke blusmiddelen voor een brandblusser."""

    def __init__(self):
        super().__init__(naam="KlBrandblusserBlusmiddel",
                         label="Brandblusser blusmiddel",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserBlusmiddel",
                         definition="Keuzelijst met de verschillende mogelijke blusmiddelen voor een brandblusser.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserBlusmiddel")

        self.add_option("poeder", "poeder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/poeder")
        self.add_option("schuim", "schuim", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/schuim")
