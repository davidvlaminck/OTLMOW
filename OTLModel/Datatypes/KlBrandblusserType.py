# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserType(Keuzelijst):
    """Keuzelijst met verschillende types van brandblussers volgens de algemene classificatie van brandblussers."""

    def __init__(self):
        super().__init__(naam="KlBrandblusserType",
                         label="Brandblusser type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserType",
                         definition="Keuzelijst met verschillende types van brandblussers volgens de algemene classificatie van brandblussers.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserType")

        self.add_option("a", "a", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/a")
        self.add_option("b", "b", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/b")
        self.add_option("c", "c", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/c")
        self.add_option("d", "d", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/d")
