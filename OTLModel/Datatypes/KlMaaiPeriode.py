# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMaaiPeriode(Keuzelijst):
    """De maand waarin het maaien wordt uitgevoerd."""

    def __init__(self):
        super().__init__(naam="KlMaaiPeriode",
                         label="Maaiperiode",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiPeriode",
                         definition="De maand waarin het maaien wordt uitgevoerd.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiPeriode")

        self.add_option("april", "april", "De maand april.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/april")
        self.add_option("mei", "mei", "De maand mei.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/mei")
        self.add_option("juni", "juni", "De maand juni.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/juni")
        self.add_option("juli", "juli", "De maand juli.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/juli")
        self.add_option("augustus", "augustus", "De maand augustus.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/augustus")
        self.add_option("september", "september", "De maand september.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/september")
        self.add_option("oktober", "oktober", "De maand oktober.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/oktober")
