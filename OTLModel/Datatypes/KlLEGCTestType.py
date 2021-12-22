from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEGCTestType(Keuzelijst):
    """Het test type van het geluidswerend scherm."""

    def __init__(self):
        super().__init__(naam="KlLEGCTestType",
                         label="Test type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCTestType",
                         definition="Het test type van het geluidswerend scherm.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCTestType")

        self.add_option("geluidsabsorptie", "geluidsabsorptie", "Proef : De ééngetalsaanduiding als waarde voor de geluidsabsorptie", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/geluidsabsorptie")
        self.add_option("luchtgeluidsisolatie", "luchtgeluidsisolatie", "Proef : De ééngetalsaanduiding voor luchtgeluidsisolatie", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/luchtgeluidsisolatie")
