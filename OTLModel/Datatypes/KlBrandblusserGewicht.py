# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserGewicht(Keuzelijst):
    """Keuzelijst met de mogelijke gewichten van brandblussers."""

    def __init__(self):
        super().__init__(naam="KlBrandblusserGewicht",
                         label="Brandblusser gewicht",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserGewicht",
                         definition="Keuzelijst met de mogelijke gewichten van brandblussers.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserGewicht")

        self.add_option("6-kg", "6 kg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserGewicht/6-kg")
        self.add_option("9-kg", "9 kg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserGewicht/9-kg")
