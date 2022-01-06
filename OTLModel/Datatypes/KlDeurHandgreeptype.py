# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurHandgreeptype(Keuzelijst):
    """Types handgrepen van deuren."""

    def __init__(self):
        super().__init__(naam="KlDeurHandgreeptype",
                         label="Deur handgreeptype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDeurHandgreeptype",
                         definition="Types handgrepen van deuren.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurHandgreeptype")

        self.add_option("klink", "klink", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/klink")
        self.add_option("handvat", "handvat", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/handvat")
        self.add_option("hendel-RWS", "hendel RWS", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/hendel-RWS")
