# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtRegelaarProtocol(Keuzelijst):
    """Beschrijft het protocol waarmee de PT-regelaar communiceert."""

    def __init__(self):
        super().__init__(naam="KlPtRegelaarProtocol",
                         label="PT-regelaar protocol",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarProtocol",
                         definition="Beschrijft het protocol waarmee de PT-regelaar communiceert.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarProtocol")

        self.add_option("R0916", "R0916", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0916")
        self.add_option("R0918", "R0918", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0918")
