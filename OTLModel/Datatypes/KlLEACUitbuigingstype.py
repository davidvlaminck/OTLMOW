# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACUitbuigingstype(Keuzelijst):
    """De mogelijke uitbuigingstypes."""

    def __init__(self):
        super().__init__(naam="KlLEACUitbuigingstype",
                         label="Uitbuigingstype",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACUitbuigingstype",
                         definition="De mogelijke uitbuigingstypes.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACUitbuigingstype")

        self.add_option("type-1", "type 1", "Uitbuiging op wegen tot 90 km/h, straal R = 10 meter", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitbuigingstype/type-1")
        self.add_option("type-2", "type 2", "Uitbuiging op wegen vanaf 90 km/h, L = 25 meter", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitbuigingstype/type-2")
