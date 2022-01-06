# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersspiegelVorm(Keuzelijst):
    """De vormen van een verkeersspiegel."""

    def __init__(self):
        super().__init__(naam="KlVerkeersspiegelVorm",
                         label="Verkeersspiegel vorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersspiegelVorm",
                         definition="De vormen van een verkeersspiegel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersspiegelVorm")

        self.add_option("rond", "rond", "ronde verkeersspiegel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersspiegelVorm/rond")
        self.add_option("rechthoekig", "rechthoekig", "rechthoekige verkeersspiegel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersspiegelVorm/rechthoekig")
