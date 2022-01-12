# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLusZichtbaarheid(Keuzelijst):
    """Is de lus zichtbaar in het wegdek of bedenkt door een toplaag."""

    def __init__(self):
        super().__init__(naam="KlMIVLusZichtbaarheid",
                         label="MIV-lus zichtbaarheid",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLusZichtbaarheid",
                         definition="Is de lus zichtbaar in het wegdek of bedenkt door een toplaag.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLusZichtbaarheid")

        self.add_option("onderlaag", "onderlaag", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusZichtbaarheid/onderlaag")
        self.add_option("toplaag", "toplaag", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusZichtbaarheid/toplaag")
