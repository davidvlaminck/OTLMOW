# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutbekledingType(Keuzelijst):
    """Types van putbekleding."""

    def __init__(self):
        super().__init__(naam="KlPutbekledingType",
                         label="Putbekleding type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutbekledingType",
                         definition="Types van putbekleding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutbekledingType")

        self.add_option("solventvrije-kunsthars", "solventvrije kunsthars", "solventvrije kunsthars", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-kunsthars")
        self.add_option("solventvrije-vezelversterkte-epoxyhars", "solventvrije vezelversterkte epoxyhars", "solventvrije vezelversterkte epoxyhars", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-vezelversterkte-epoxyhars")
