# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardWBSS(Keuzelijst):
    """De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen."""

    def __init__(self):
        super().__init__(naam="KlAardWBSS",
                         label="Aard van waterdoorlatende betonstraatsteen",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAardWBSS",
                         definition="De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardWBSS")

        self.add_option("met-drainageopeningen", "met drainageopeningen", "Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-drainageopeningen")
        self.add_option("met-verbrede-voegen", "met verbrede voegen", "Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-verbrede-voegen")
        self.add_option("poreus-beton", "poreus beton", "Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert doorheen de betonstraatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/poreus-beton")
