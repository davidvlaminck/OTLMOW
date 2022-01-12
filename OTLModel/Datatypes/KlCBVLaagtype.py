# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVLaagtype(Keuzelijst):
    """Bepaling van het laagtype van de cement/beton verharding."""

    def __init__(self):
        super().__init__(naam="KlCBVLaagtype",
                         label="CBV laagtype",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVLaagtype",
                         definition="Bepaling van het laagtype van de cement/beton verharding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVLaagtype")

        self.add_option("eenlaagse-betonverharding", "eenlaagse betonverharding", "Betonverharding die in één laag aangelegd wordt. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVLaagtype/eenlaagse-betonverharding")
        self.add_option("tweelaagse-betonverharding", "tweelaagse betonverharding", "Betonverharding die in twee lagen aangelegd wordt. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVLaagtype/tweelaagse-betonverharding")
