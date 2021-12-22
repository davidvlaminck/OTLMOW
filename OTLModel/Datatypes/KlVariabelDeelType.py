from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVariabelDeelType(Keuzelijst):
    """Types van het variabel deel van een overstortrand."""

    def __init__(self):
        super().__init__(naam="KlVariabelDeelType",
                         label="Variabel deel type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVariabelDeelType",
                         definition="Types van het variabel deel van een overstortrand.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabelDeelType")

        self.add_option("schotbalk", "schotbalk", "schotbalk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/schotbalk")
        self.add_option("overstortplaat", "overstortplaat", "overstortplaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/overstortplaat")
