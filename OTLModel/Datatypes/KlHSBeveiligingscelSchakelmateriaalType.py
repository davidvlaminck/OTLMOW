# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelSchakelmateriaalType(Keuzelijst):
    """Type van schakelmateriaal."""

    def __init__(self):
        super().__init__(naam="KlHSBeveiligingscelSchakelmateriaalType",
                         label="HS-beveiligingscel schakelmateriaal type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelSchakelmateriaalType",
                         definition="Type van schakelmateriaal.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelSchakelmateriaalType")

        self.add_option("RMU-2KT", "RMU 2KT", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/RMU-2KT")
        self.add_option("RMU-3KT", "RMU 3KT", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/RMU-3KT")
        self.add_option("metaalomsloten-celstruktuur", "metaalomsloten celstruktuur", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/metaalomsloten-celstruktuur")
        self.add_option("metal-clad-schakelvelden", "metal-clad schakelvelden", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/metal-clad-schakelvelden")
        self.add_option("modulaire-schakelvelden", "modulaire schakelvelden", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/modulaire-schakelvelden")
        self.add_option("open-celstruktuur", "open celstruktuur", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/open-celstruktuur")
