# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerType(Keuzelijst):
    """De soort omvorming die gebeurt er in de omvormer."""

    def __init__(self):
        super().__init__(naam="KlOmvormerType",
                         label="Omvormer type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerType",
                         definition="De soort omvorming die gebeurt er in de omvormer.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerType")

        self.add_option("UTP-Coax", "UTP-Coax", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Coax")
        self.add_option("UTP-(Serieel)-UTP", "UTP (Serieel)-UTP", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-(Serieel)-UTP")
        self.add_option("Decoder", "Decoder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Decoder")
        self.add_option("UTP-UTP-(serieel)", "UTP-UTP (serieel)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-UTP-(serieel)")
        self.add_option("Encoder", "Encoder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Encoder")
        self.add_option("draadloos-utp", "Draadloos-UTP", "Draadloos-UTP", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/draadloos-utp")
        self.add_option("Coax-UTP", "Coax-UTP", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Coax-UTP")
        self.add_option("Glasvezel-UTP", "Glasvezel-UTP", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Glasvezel-UTP")
        self.add_option("UTP-Glasvezel", "UTP-Glasvezel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Glasvezel")
        self.add_option("utp-draadloos", "UTP-Draadloos", "UTP-Draadloos", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/utp-draadloos")
