# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignalisatieReferentiepuntType(Keuzelijst):
    """Een keuzelijst om het referentiepunt type te bepalen."""

    def __init__(self):
        super().__init__(naam="KlSignalisatieReferentiepuntType",
                         label="Signalisatie referentiepunt type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignalisatieReferentiepuntType",
                         definition="Een keuzelijst om het referentiepunt type te bepalen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignalisatieReferentiepuntType")

        self.add_option("hectometerpalen-in-kunststof", "hectometerpalen in kunststof", "Een kleine paal in kunststof die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpalen-in-kunststof")
        self.add_option("hectometerpunt-aan-ronde-steun", "hectometerpunt aan ronde steun", "Een hectometerbord bevestigd aan een ronde steun die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpunt-aan-ronde-steun")
        self.add_option("hectometerpunt-op-horizontale-wand", "hectometerpunt op horizontale wand", "Een hectometerbord bevestigd tegen een horizontale wand (zoals bv een New Jersey) die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpunt-op-horizontale-wand")
        self.add_option("kilometerpalen-in-kunststof", "kilometerpalen in kunststof", "Een kleine paal in kunststof die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpalen-in-kunststof")
        self.add_option("kilometerpunt-aan-ronde-steun", "kilometerpunt aan ronde steun", "Een kilometerbord bevestigd aan een ronde steun die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpunt-aan-ronde-steun")
        self.add_option("kilometerpunt-op-horizontale-wand", "kilometerpunt op horizontale wand", "Een kilometerbord bevestigd tegen een horizontale wand (zoals bv een New Jersey) die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpunt-op-horizontale-wand")
