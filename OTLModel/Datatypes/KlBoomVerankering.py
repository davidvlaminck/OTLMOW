# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomVerankering(Keuzelijst):
    """De verschillende manieren van verankering van een boom."""

    def __init__(self):
        super().__init__(naam="KlBoomVerankering",
                         label="Boom verankering",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomVerankering",
                         definition="De verschillende manieren van verankering van een boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomVerankering")

        self.add_option("bovengronds", "bovengronds", "De constructie voor de stabiliteit van de boom bevindt zich boven de grond", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankering/bovengronds")
        self.add_option("ondergronds", "ondergronds", "De constructie voor de stabiliteit van de boom bevindt zich volledig onder de grond", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankering/ondergronds")
