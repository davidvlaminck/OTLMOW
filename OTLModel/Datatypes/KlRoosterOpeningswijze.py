# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRoosterOpeningswijze(Keuzelijst):
    """Deze keuzelijst geeft de manier aan hoe het rooster geopend kan worden."""

    def __init__(self):
        super().__init__(naam="KlRoosterOpeningswijze",
                         label="Rooster openingswijze",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRoosterOpeningswijze",
                         definition="Deze keuzelijst geeft de manier aan hoe het rooster geopend kan worden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRoosterOpeningswijze")

        self.add_option("scharnierend", "scharnierend", "scharnierend", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/scharnierend")
        self.add_option("uitneembaar", "uitneembaar", "uitneembaar", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/uitneembaar")
        self.add_option("ovaal-deksel", "ovaal deksel", "ovaal deksel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/ovaal-deksel")
