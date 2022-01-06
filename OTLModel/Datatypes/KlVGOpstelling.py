# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVGOpstelling(Keuzelijst):
    """Beschrijft de oriëntatie van het geplaatste schermelement tov de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn."""

    def __init__(self):
        super().__init__(naam="KlVGOpstelling",
                         label="Vlak geluidschermelement opstelling",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVGOpstelling",
                         definition="Beschrijft de oriëntatie van het geplaatste schermelement tov de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVGOpstelling")

        self.add_option("loodrecht-op-maaiveld", "loodrecht op maaiveld", "loodrecht op maaiveld", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/loodrecht-op-maaiveld")
        self.add_option("schuin-naar-achter-hellend", "schuin naar achter hellend", "schuin naar achter hellend t.o.v. de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/schuin-naar-achter-hellend")
        self.add_option("schuin-naar-voor-hellend", "schuin naar voor hellend", "schuin naar voor hellend t.o.v. de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/schuin-naar-voor-hellend")
