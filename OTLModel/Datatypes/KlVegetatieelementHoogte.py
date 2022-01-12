# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieelementHoogte(Keuzelijst):
    """De orde van hoogte van een vegetatie-element."""

    def __init__(self):
        super().__init__(naam="KlVegetatieelementHoogte",
                         label="Vegetatieelement hoogte",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieelementHoogte",
                         definition="De orde van hoogte van een vegetatie-element.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieelementHoogte")

        self.add_option("0--7-meter", "0 -7 meter", "0 -7 meter", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementHoogte/0--7-meter")
        self.add_option("7---20-meter", "7 - 20 meter", "7 - 20 meter", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementHoogte/7---20-meter")
        self.add_option("groter-dan-20-meter", "groter dan 20 meter", "> 20 meter", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementHoogte/groter-dan-20-meter")
