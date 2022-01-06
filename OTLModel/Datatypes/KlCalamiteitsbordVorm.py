# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCalamiteitsbordVorm(Keuzelijst):
    """Vormen van het calamiteitsbord."""

    def __init__(self):
        super().__init__(naam="KlCalamiteitsbordVorm",
                         label="Calamiteitsbord vorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordVorm",
                         definition="Vormen van het calamiteitsbord.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordVorm")

        self.add_option("rechthoekig", "rechthoekig", "Een rechthoekig calamiteitsbord.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordVorm/rechthoekig")
        self.add_option("ruitvormig", "ruitvormig", "Een ruitvormig calamiteitsbord.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordVorm/ruitvormig")
