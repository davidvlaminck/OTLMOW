# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRackType(Keuzelijst):
    """Lijst met gestandaardiseerde en niet-gestandaardiseerde types rack in gebruik bij de assetbeheerder."""

    def __init__(self):
        super().__init__(naam="KlRackType",
                         label="rack type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRackType",
                         definition="Lijst met gestandaardiseerde en niet-gestandaardiseerde types rack in gebruik bij de assetbeheerder.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRackType")

        self.add_option("19-inch", "19-inch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/19-inch")
        self.add_option("21-inch", "21-inch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/21-inch")
        self.add_option("MIVSATRack", "MIVSATRack", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/MIVSATRack")
        self.add_option("DIN-rail", "DIN-rail", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/DIN-rail")
        self.add_option("MIVLVERack", "MIVLVERack", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/MIVLVERack")
