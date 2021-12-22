from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVegetatieWortel(Keuzelijst):
    """De verschillende opties van hoe de wortel was bij aanplanting."""

    def __init__(self):
        super().__init__(naam="KlVegetatieWortel",
                         label="Vegetatie wortel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieWortel",
                         definition="De verschillende opties van hoe de wortel was bij aanplanting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieWortel")

        self.add_option("naakt", "naakt", "Wortels waarrond geen grond aanwezig is", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/naakt")
        self.add_option("draadkluit", "draadkluit", "De wortels zitten in een met draad ingebonden kluit aarde", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/draadkluit")
        self.add_option("container", "container", "De wortels zitten in een container of pot bij aanlevering en aanplant.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/container")
        self.add_option("kluit", "kluit", "De wortels zijn omringd met aarde.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/kluit")
