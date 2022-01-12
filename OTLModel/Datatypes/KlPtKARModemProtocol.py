# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtKARModemProtocol(Keuzelijst):
    """Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren."""

    def __init__(self):
        super().__init__(naam="KlPtKARModemProtocol",
                         label="PT-KAR-modem protocol",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtKARModemProtocol",
                         definition="Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtKARModemProtocol")

