# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSoftwareLicentie(Keuzelijst):
    """De licentievorm van de software."""

    def __init__(self):
        super().__init__(naam="KlSoftwareLicentie",
                         label="Software licentie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSoftwareLicentie",
                         definition="De licentievorm van de software.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSoftwareLicentie")

        self.add_option("commercieel", "commercieel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/commercieel")
        self.add_option("shareware", "shareware", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/shareware")
        self.add_option("freeware", "freeware", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/freeware")
        self.add_option("open-source-BSD", "open source BSD", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/open-source-BSD")
        self.add_option("open-source-Apache", "open source Apache", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/open-source-Apache")
        self.add_option("open-source-GPL", "open source GPL", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/open-source-GPL")
