# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringVerschuindSoort(Keuzelijst):
    """Soorten van de schuine dwarse markering."""

    def __init__(self):
        super().__init__(naam="KlDwarseMarkeringVerschuindSoort",
                         label="Dwarse markering soort verschuind",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringVerschuindSoort",
                         definition="Soorten van de schuine dwarse markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringVerschuindSoort")

        self.add_option("fietsoversteekplaats-met-blokken-(FOP)-schuin", "fietsoversteekplaats met blokken (FOP) schuin", "Een oversteekplaats voor fietsers gemarkeerd door witte parallellogrammen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringVerschuindSoort/fietsoversteekplaats-met-blokken-(FOP)-schuin")
