# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordconceptStatus(Keuzelijst):
    """Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt."""

    def __init__(self):
        super().__init__(naam="KlVerkeersbordconceptStatus",
                         label="VerkeersbordconceptStatus",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordconceptStatus",
                         definition="Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt.",
                         usagenote="Bijvoorbeeld: stabiel, onstabiel, afgeschaft. Een bord met snelheidslimiet van 60 km/u is bijvoorbeeld afgeschaft.",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordconceptStatus")

        self.add_option("afgeschaft", "afgeschaft", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/afgeschaft")
        self.add_option("stabiel", "stabiel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/stabiel")
