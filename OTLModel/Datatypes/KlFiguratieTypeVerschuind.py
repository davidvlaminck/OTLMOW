# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieTypeVerschuind(Keuzelijst):
    """Types van verschuinde figuratiemarkering."""

    def __init__(self):
        super().__init__(naam="KlFiguratieTypeVerschuind",
                         label="Figuratie type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieTypeVerschuind",
                         definition="Types van verschuinde figuratiemarkering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieTypeVerschuind")

        self.add_option("STOP-(smal-schuin)", "STOP (smal schuin)", "Lettermarkering STOP (smal schuin)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieTypeVerschuind/STOP-(smal-schuin)")
        self.add_option("groot-(schuin)", "groot (schuin)", "Omgekeerde driehoek markering groot en schuin type.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieTypeVerschuind/groot-(schuin)")
