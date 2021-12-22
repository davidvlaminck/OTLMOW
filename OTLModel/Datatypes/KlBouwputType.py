from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBouwputType(Keuzelijst):
    """Het type van bouwput."""

    def __init__(self):
        super().__init__(naam="KlBouwputType",
                         label="Bouwput type.",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBouwputType",
                         definition="Het type van bouwput.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBouwputType")

        self.add_option("bouwput", "bouwput", "bouwput", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/bouwput")
        self.add_option("ontvangstput", "ontvangstput", "ontvangstput", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/ontvangstput")
        self.add_option("persput", "persput", "persput", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/persput")
        self.add_option("intredeput", "intredeput", "intredeput", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/intredeput")
