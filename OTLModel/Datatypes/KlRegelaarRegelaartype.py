# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRegelaarRegelaartype(Keuzelijst):
    """Keuzelijst met verschillende types verkeersregelaars."""

    def __init__(self):
        super().__init__(naam="KlRegelaarRegelaartype",
                         label="Regelaar regelaartype",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRegelaarRegelaartype",
                         definition="Keuzelijst met verschillende types verkeersregelaars.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRegelaarRegelaartype")

        self.add_option("type-0", "type 0", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-0")
        self.add_option("type-1", "type 1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-1")
        self.add_option("type-2", "type 2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-2")
        self.add_option("type-3", "type 3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-3")
