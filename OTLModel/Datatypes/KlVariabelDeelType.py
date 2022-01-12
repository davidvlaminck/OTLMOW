# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVariabelDeelType(Keuzelijst):
    """Types van het variabel deel van een overstortrand."""

    def __init__(self):
        super().__init__(naam="KlVariabelDeelType",
                         label="Variabel deel type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVariabelDeelType",
                         definition="Types van het variabel deel van een overstortrand.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabelDeelType")

        self.add_option("overstortplaat", "overstortplaat", "overstortplaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/overstortplaat")
        self.add_option("schotbalk", "schotbalk", "schotbalk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/schotbalk")
