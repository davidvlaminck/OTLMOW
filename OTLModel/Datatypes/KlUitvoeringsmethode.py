# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringsmethode(Keuzelijst):
    """Manier van uitvoeren en aanbrengen van beton."""

    def __init__(self):
        super().__init__(naam="KlUitvoeringsmethode",
                         label="Uitvoeringsmethode",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlUitvoeringsmethode",
                         definition="Manier van uitvoeren en aanbrengen van beton.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringsmethode")

        self.add_option("geprefabriceerd", "Geprefabriceerd", "Het beton is geprefabriceerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/geprefabriceerd")
        self.add_option("ter-plaatse-gestort-met-bekisting", "Ter plaatse gestort met bekisting", "Het beton wordt ter plaatste gestort met bekisting.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort-met-bekisting")
        self.add_option("ter-plaatse-gestort-zonder-bekisting", "Ter plaatse gestort zonder bekisting", "Het beton wordt ter plaatste gestort zonder bekisting.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort-zonder-bekisting")
