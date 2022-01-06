# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLusUitslijprichting(Keuzelijst):
    """De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting."""

    def __init__(self):
        super().__init__(naam="KlMIVLusUitslijprichting",
                         label="MIV-lus uitslijprichting",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLusUitslijprichting",
                         definition="De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLusUitslijprichting")

        self.add_option("links", "links", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusUitslijprichting/links")
        self.add_option("rechts", "rechts", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusUitslijprichting/rechts")
