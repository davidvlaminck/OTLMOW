# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlooibakenType(Keuzelijst):
    """ vormen van een plooibaken."""

    def __init__(self):
        super().__init__(naam="KlPlooibakenType",
                         label="Plooibaken type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlooibakenType",
                         definition=" vormen van een plooibaken.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlooibakenType")

        self.add_option("plooibaken-diameter-80-mm---M16", "plooibaken diameter 80 mm - M16", "Plooibaken diameter 80 mm – M16", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-80-mm---M16")
        self.add_option("plooibaken-diameter-80-mm---M24", "plooibaken diameter 80 mm - M24", "Plooibaken diameter 80 mm – M24", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-80-mm---M24")
        self.add_option("plooibaken-diameter-130-mm---M24", "plooibaken diameter 130 mm - M24", "Plooibaken diameter 130 mm – M24", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-130-mm---M24")
        self.add_option("verkeerszuil", "verkeerszuil", "Verkeerszuil", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/verkeerszuil")
