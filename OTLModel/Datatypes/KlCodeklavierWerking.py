# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCodeklavierWerking(Keuzelijst):
    """Een keuzelijst met werkingsprincipes van een codeklavier."""

    def __init__(self):
        super().__init__(naam="KlCodeklavierWerking",
                         label="Codeklavier werking",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCodeklavierWerking",
                         definition="Een keuzelijst met werkingsprincipes van een codeklavier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCodeklavierWerking")

        self.add_option("cijfercodeslot", "cijfercodeslot", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot")
        self.add_option("drukknop", "drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/drukknop")
        self.add_option("cijfercodeslot-met-drukknop", "cijfercodeslot met drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot-met-drukknop")
