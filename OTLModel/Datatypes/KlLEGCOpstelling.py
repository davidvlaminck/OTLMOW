# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCOpstelling(Keuzelijst):
    """De opstellingen van de geluidswerende constructie."""

    def __init__(self):
        super().__init__(naam="KlLEGCOpstelling",
                         label="Opstelling",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpstelling",
                         definition="De opstellingen van de geluidswerende constructie.",
                         usagenote="Klasse uit gebruik sinds versie 2.0.0",
                         deprecated_version="2.0.0",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpstelling")

        self.add_option("concaaf", "concaaf", "Concave opstelling t.o.v. de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/concaaf")
        self.add_option("schuin-naar-achter-hellend", "schuin naar achter hellend", "schuin naar achter hellend t.o.v. de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/schuin-naar-achter-hellend")
        self.add_option("schuin-naar-voor-hellend", "schuin naar voor hellend", "schuin naar voor hellend t.o.v. de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/schuin-naar-voor-hellend")
        self.add_option("verticaal", "verticaal", "verticaal t.o.v. de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/verticaal")
