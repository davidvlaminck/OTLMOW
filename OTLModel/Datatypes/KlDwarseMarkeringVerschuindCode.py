# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringVerschuindCode(Keuzelijst):
    """Codes van de schuine dwarse markering."""

    def __init__(self):
        super().__init__(naam="KlDwarseMarkeringVerschuindCode",
                         label="Dwarse markering code verschuind",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringVerschuindCode",
                         definition="Codes van de schuine dwarse markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringVerschuindCode")

        self.add_option("FOP-sch", "FOP-sch", "Fietsoversteekplaats met blokken schuin", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringVerschuindCode/FOP-sch")
