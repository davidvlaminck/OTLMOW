# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoppinzuilType(Keuzelijst):
    """De types van een analoge hoppinzuil."""

    def __init__(self):
        super().__init__(naam="KlHoppinzuilType",
                         label="Hoppinzuil type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoppinzuilType",
                         definition="De types van een analoge hoppinzuil.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoppinzuilType")

        self.add_option("analoog-groot", "Analoog groot", "Hoppinzuil met een minimale afmeting van 55x10x280 cm waarop de veranderlijke informatie analoog (op papier/sticker) wordt weergegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoppinzuilType/analoog-groot")
        self.add_option("analoog-mini", "Analoog mini", "Hoppinzuil met een minimale afmeting van 40x3x200 cm waarop de veranderlijke informatie analoog (op papier/sticker) wordt weergegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoppinzuilType/analoog-mini")
