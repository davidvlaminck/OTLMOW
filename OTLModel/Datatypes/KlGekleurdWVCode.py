# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGekleurdWVCode(Keuzelijst):
    """Codes voor een gekleurd wegvlak."""

    def __init__(self):
        super().__init__(naam="KlGekleurdWVCode",
                         label="Gekleurd WV code",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGekleurdWVCode",
                         definition="Codes voor een gekleurd wegvlak.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGekleurdWVCode")

        self.add_option("GW-FOP", "GW-FOP", "Gekleurd wegvlak voor fietsoversteekplaats met blokken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FOP")
        self.add_option("GW-FP", "GW-FP", "Gekleurd wegvlak voor fietsoversteekplaats met lijnen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FP")
        self.add_option("GW-FSUG", "GW-FSUG", "Gekleurd wegvlak voor fietssuggestiestrook (oker,grijs).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FSUG")
        self.add_option("GW-FSUG-A", "GW-FSUG-A", "Gekleurd wegvlak voor fietssuggestiestrook (groen,geel,rood).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FSUG-A")
        self.add_option("GW-MID", "GW-MID", "Gekleurd wegvlak voor middengeleider(bv.groene strook)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-MID")
        self.add_option("GW-MV", "GW-MV", "Gekleurd wegvlak voor parkeerplaats mindervaliden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-MV")
        self.add_option("GW-OFOS", "GW-OFOS", "Gekleurd wegvlak voor voor OFOS.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-OFOS")
        self.add_option("GW-OFOS-VAR", "GW-OFOS-VAR", "Gekleurd wegvlak voor OFOS variant.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-OFOS-VAR")
        self.add_option("GW-PLAT", "GW-PLAT", "Gekleurd wegvlak voor verkeersplateau.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-PLAT")
        self.add_option("GW-VOP", "GW-VOP", "Gekleurd wegvlak voor voetgangers-oversteekplaats.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-VOP")
