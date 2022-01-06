# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACTypeEindstuk(Keuzelijst):
    """De verschillende types eindstukken."""

    def __init__(self):
        super().__init__(naam="KlLEACTypeEindstuk",
                         label="Type eindstuk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACTypeEindstuk",
                         definition="De verschillende types eindstukken.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACTypeEindstuk")

        self.add_option("uitgebogen", "uitgebogen", "uitgebogen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/uitgebogen")
        self.add_option("schelp", "schelp", "schelp", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/schelp")
        self.add_option("naar-beneden-afgebogen", "naar beneden afgebogen", "naar beneden afgebogen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/naar-beneden-afgebogen")
