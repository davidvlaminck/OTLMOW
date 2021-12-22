from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlGekleurdWVSoort(Keuzelijst):
    """Types van gekleurd wegvlak."""

    def __init__(self):
        super().__init__(naam="KlGekleurdWVSoort",
                         label="Gekleurd WV type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGekleurdWVSoort",
                         definition="Types van gekleurd wegvlak.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGekleurdWVSoort")

        self.add_option("fietspad-(met-lijnen)", "fietspad (met lijnen)", "Gekleurd wegvlak als fietspad (met lijnen).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fietspad-(met-lijnen)")
        self.add_option("fietsoversteekplaats-met-blokken-(FOP)", "fietsoversteekplaats met blokken (FOP)", "Gekleurd wegvlak als fietsoversteekplaats met blokken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fietsoversteekplaats-met-blokken-(FOP)")
        self.add_option("fiets-suggestiestrook", "fiets suggestiestrook", "Gekleurd wegvlak als fiets suggestiestrook.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fiets-suggestiestrook")
        self.add_option("parkeerplaats-mindervaliden", "parkeerplaats mindervaliden", "Gekleurd wegvlak als parkeerplaats mindervaliden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/parkeerplaats-mindervaliden")
        self.add_option("OFOS-(Opgeblazen-fietsopstelstrook)", "OFOS (Opgeblazen fietsopstelstrook)", "Gekleurd wegvlak als OFOS.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/OFOS-(Opgeblazen-fietsopstelstrook)")
        self.add_option("OFOS-variant", "OFOS variant", "Gekleurd wegvlak als OFOS variant.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/OFOS-variant")
        self.add_option("middengeleider-(Bv.-Groene-strook)", "middengeleider (Bv. Groene strook)", "Gekleurd wegvlak als middengeleider.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/middengeleider-(Bv.-Groene-strook)")
        self.add_option("verkeersplateau", "verkeersplateau", "Gekleurd wegvlak als verkeersplateau.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/verkeersplateau")
        self.add_option("voetgangers-oversteekplaats", "voetgangers-oversteekplaats", "Gekleurd wegvlak als voetgangers-oversteekplaats.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/voetgangers-oversteekplaats")
