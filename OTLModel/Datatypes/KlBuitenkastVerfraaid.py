# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBuitenkastVerfraaid(Keuzelijst):
    """Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund."""

    def __init__(self):
        super().__init__(naam="KlBuitenkastVerfraaid",
                         label="Verfraaiing buitenkast",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlBuitenkastVerfraaid",
                         definition="Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBuitenkastVerfraaid")

        self.add_option("ja", "ja", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja")
        self.add_option("ja-niet-vergund", "ja niet vergund", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja-niet-vergund")
        self.add_option("nee", "nee", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/nee")
