# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCGeluidskarakteristiek(Keuzelijst):
    """De geluidskarakteristieken van de geluidswerende constructie."""

    def __init__(self):
        super().__init__(naam="KlLEGCGeluidskarakteristiek",
                         label="Geluidskarakteristiek",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCGeluidskarakteristiek",
                         definition="De geluidskarakteristieken van de geluidswerende constructie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCGeluidskarakteristiek")

        self.add_option("absorberend", "absorberend", "De geluidsgolven worden gedeeltelijk niet weerkaatst door de geluidswerende constructie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCGeluidskarakteristiek/absorberend")
        self.add_option("bi-absorberend", "bi-absorberend", "De geluidsgolven worden gedeeltelijk niet weerkaatst door de geluidswerende constructie (langs beide zijden).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCGeluidskarakteristiek/bi-absorberend")
        self.add_option("reflecterend", "reflecterend", "reflecterend", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCGeluidskarakteristiek/reflecterend")
