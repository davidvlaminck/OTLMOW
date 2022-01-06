# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPoortconfiguratieRichting(Keuzelijst):
    """De richting waarin de poort openstaat."""

    def __init__(self):
        super().__init__(naam="KlPoortconfiguratieRichting",
                         label="Poortconfiguratie richting",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPoortconfiguratieRichting",
                         definition="De richting waarin de poort openstaat.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoortconfiguratieRichting")

        self.add_option("uitgaand", "uitgaand", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/uitgaand")
        self.add_option("ingaand", "ingaand", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/ingaand")
