# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkelemGebruik(Keuzelijst):
    """Keuzelijst met de verschillende mogelijke netwerkstructuren waarbinnen een netwerkelement kan ingezet worden."""

    def __init__(self):
        super().__init__(naam="KlNetwerkelemGebruik",
                         label="Netwerkelement gebruik",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkelemGebruik",
                         definition="Keuzelijst met de verschillende mogelijke netwerkstructuren waarbinnen een netwerkelement kan ingezet worden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkelemGebruik")

        self.add_option("4g-wireless-router", "4G wireless router", "Het netwerkelement wordt gebruikt binnen een 4G draadloos netwerk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/4g-wireless-router")
        self.add_option("cen", "CEN", "Het netwerkelement wordt gebruikt binnen het CEN netwerk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/cen")
        self.add_option("sdh", "SDH", "Het netwerkelement wordt gebruikt binnen het SDH netwerk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/sdh")
        self.add_option("otn", "OTN", "Het netwerkelement wordt gebruikt binnen het optisch transport netwerk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/otn")
        self.add_option("l2-switch", "L2-switch", "Het netwerkelement wordt gebruikt binnen de L2 netwerkstructuur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/l2-switch")
        self.add_option("l3-switch", "L3-switch", "Het netwerkelement wordt gebruikt binnen de L3 netwerkstructuur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/l3-switch")
