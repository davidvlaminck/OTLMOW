# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSleufUitvoering(Keuzelijst):
    """Uitvoeringen van de sleuf."""

    def __init__(self):
        super().__init__(naam="KlSleufUitvoering",
                         label="Sleuf uitvoering",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSleufUitvoering",
                         definition="Uitvoeringen van de sleuf.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSleufUitvoering")

        self.add_option("open-sleuf", "open sleuf", "open sleuf", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/open-sleuf")
        self.add_option("beschoeide-sleuf", "beschoeide sleuf", "beschoeide sleuf", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/beschoeide-sleuf")
        self.add_option("beschoeide-sleuf-met-voorafgraving", "beschoeide sleuf met voorafgraving", "beschoeide sleuf met voorafgraving", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/beschoeide-sleuf-met-voorafgraving")
        self.add_option("waterdicht-beschoeide-sleuf-met-damplanken", "waterdicht beschoeide sleuf met damplanken", "waterdicht beschoeide sleuf met damplanken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/waterdicht-beschoeide-sleuf-met-damplanken")
        self.add_option("onderdoorpersing", "onderdoorpersing", "onderdoorpersing", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/onderdoorpersing")
        self.add_option("directional-drilling", "directional drilling", "directional drilling", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/directional-drilling")
