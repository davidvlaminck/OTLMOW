# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntiparkeerpaalMateriaal(Keuzelijst):
    """Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal."""

    def __init__(self):
        super().__init__(naam="KlAntiparkeerpaalMateriaal",
                         label="Antiparkeerpaal materiaal",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntiparkeerpaalMateriaal",
                         definition="Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntiparkeerpaalMateriaal")

        self.add_option("hout", "hout", "Keuze hout voor het antiparkeerpaal materiaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/hout")
        self.add_option("kunststof", "kunststof", "Keuze kunststof voor het antiparkeerpaal materiaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/kunststof")
        self.add_option("metaal", "metaal", "Keuze metaal voor het antiparkeerpaal materiaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/metaal")
