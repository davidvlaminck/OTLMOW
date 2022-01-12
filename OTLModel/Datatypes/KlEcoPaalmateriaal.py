# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoPaalmateriaal(Keuzelijst):
    """Materialen van de paal in het ecoraster."""

    def __init__(self):
        super().__init__(naam="KlEcoPaalmateriaal",
                         label="Paalmateriaal",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoPaalmateriaal",
                         definition="Materialen van de paal in het ecoraster.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoPaalmateriaal")

        self.add_option("hout-Kastanje", "hout Kastanje", "Een houten paal van kastanje hout.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPaalmateriaal/hout-Kastanje")
        self.add_option("hout-Robina", "hout Robina", "Een houten paal van robina hout.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPaalmateriaal/hout-Robina")
        self.add_option("metaal", "metaal", "Een metalen paal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPaalmateriaal/metaal")
