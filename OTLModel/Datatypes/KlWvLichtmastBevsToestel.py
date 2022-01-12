# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastBevsToestel(Keuzelijst):
    """De standaard bevestigingen van verlichtingstoestellen aan lichtmasten."""

    def __init__(self):
        super().__init__(naam="KlWvLichtmastBevsToestel",
                         label="Bevestiging voor wegverlichtingstoestellen",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastBevsToestel",
                         definition="De standaard bevestigingen van verlichtingstoestellen aan lichtmasten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastBevsToestel")

        self.add_option("kroon", "kroon", "keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/kroon")
        self.add_option("mediaanbalk-H", "mediaanbalk H", "keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-H")
        self.add_option("mediaanbalk-I", "mediaanbalk I", "keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-I")
        self.add_option("mediaanbalk-U", "mediaanbalk U", "keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-U")
        self.add_option("ossenkop", "ossenkop", "keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/ossenkop")
        self.add_option("paaltop-108mm", "paaltop 108mm", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-108mm")
        self.add_option("paaltop-60mm", "paaltop 60mm", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-60mm")
        self.add_option("paaltop-76mm", "paaltop 76mm", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-76mm")
        self.add_option("plaat", "plaat", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/plaat")
        self.add_option("t-stuk", "t-stuk", "keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/t-stuk")
