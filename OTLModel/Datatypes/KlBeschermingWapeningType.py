# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermingWapeningType(Keuzelijst):
    """De mogelijke wapeningen gebruikt bij de oa. fundering (wapeningsnet,geotextiel,geogrids)."""

    def __init__(self):
        super().__init__(naam="KlBeschermingWapeningType",
                         label="Bescherming wapening type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingWapeningType",
                         definition="De mogelijke wapeningen gebruikt bij de oa. fundering (wapeningsnet,geotextiel,geogrids).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingWapeningType")

        self.add_option("wapeningsnet", "wapeningsnet", "Keuzelijst voor de wapening gebruikt bij de fundering (wapeningsnet,geotextiel,geogrids)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/wapeningsnet")
        self.add_option("gelast-geplastificeerd-gaas", "gelast geplastificeerd gaas", "gelast geplastificeerd gaas", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/gelast-geplastificeerd-gaas")
        self.add_option("geogrids", "geogrids", "Een roosterweefsel dat als een soort funderingsrooster wordt toegepast", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/geogrids")
        self.add_option("honinggraatstructuur", "honinggraatstructuur", "Een wapening_bescherming met honinggraatstructuur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/honinggraatstructuur")
