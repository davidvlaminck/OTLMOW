# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraDetectieprincipe(Keuzelijst):
    """Keuzelijst met detectieprincipes voor Detectiecamera."""

    def __init__(self):
        super().__init__(naam="KlDetectiecameraDetectieprincipe",
                         label="Detectiecamera detectieprincipe",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraDetectieprincipe",
                         definition="Keuzelijst met detectieprincipes voor Detectiecamera.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraDetectieprincipe")

        self.add_option("optisch", "optisch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/optisch")
        self.add_option("thermografisch", "thermografisch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/thermografisch")
