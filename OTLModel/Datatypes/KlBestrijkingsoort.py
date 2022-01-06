# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingsoort(Keuzelijst):
    """Soorten van bestrijking."""

    def __init__(self):
        super().__init__(naam="KlBestrijkingsoort",
                         label="Bestrijkingsoort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingsoort",
                         definition="Soorten van bestrijking.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingsoort")

        self.add_option("eenlaagse-met-enkele-begrinding-(EBEB)", "eenlaagse met enkele begrinding (EBEB)", "éénlaagse bestrijking met enkele begrinding (EBEB)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingsoort/eenlaagse-met-enkele-begrinding-(EBEB)")
        self.add_option("eenlaagse-met-dubbele-begrinding-(EBDB)", "eenlaagse met dubbele begrinding (EBDB)", "éénlaagse bestrijking met dubbele begrinding (EBDB)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingsoort/eenlaagse-met-dubbele-begrinding-(EBDB)")
        self.add_option("tweelaagse-(TB)", "tweelaagse (TB)", "tweelaagse bestrijking (TB)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingsoort/tweelaagse-(TB)")
