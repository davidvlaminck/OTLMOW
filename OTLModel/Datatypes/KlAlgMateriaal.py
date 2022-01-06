# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMateriaal(Keuzelijst):
    """Het materiaal waaruit een object voornamelijk gebouwd is."""

    def __init__(self):
        super().__init__(naam="KlAlgMateriaal",
                         label="Materiaal soorten",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgMateriaal",
                         definition="Het materiaal waaruit een object voornamelijk gebouwd is.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMateriaal")

        self.add_option("kunstof", "kunstof", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunstof")
        self.add_option("kunststof", "kunststof", "kunststof", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunststof")
        self.add_option("glasvezelversterkt-polyester", "glasvezelversterkt polyester", "glasvezelversterkt polyester", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/glasvezelversterkt-polyester")
        self.add_option("aluminium", "aluminium", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/aluminium")
        self.add_option("houtvezelbeton", "houtvezelbeton", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/houtvezelbeton")
        self.add_option("roestvrijstaal", "roestvrijstaal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/roestvrijstaal")
        self.add_option("beton", "beton", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/beton")
        self.add_option("hout", "hout", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/hout")
        self.add_option("staal", "staal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/staal")
