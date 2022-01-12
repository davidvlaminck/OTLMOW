# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDunneOverlagingType(Keuzelijst):
    """Types van dunne overlaging."""

    def __init__(self):
        super().__init__(naam="KlDunneOverlagingType",
                         label="Dunne overlaging type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDunneOverlagingType",
                         definition="Types van dunne overlaging.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDunneOverlagingType")

        self.add_option("SME-D1", "SME-D1", "SME-D1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D1")
        self.add_option("SME-D2", "SME-D2", "SMA-D2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D2")
        self.add_option("antisliplaag", "antisliplaag", "antisliplaag", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/antisliplaag")
