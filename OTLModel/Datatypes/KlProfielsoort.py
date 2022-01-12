# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlProfielsoort(Keuzelijst):
    """Het type profiel (de meest genormeerde types)."""

    def __init__(self):
        super().__init__(naam="KlProfielsoort",
                         label="Profielsoort",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlProfielsoort",
                         definition="Het type profiel (de meest genormeerde types).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlProfielsoort")

        self.add_option("hd", "HD", "Breedflensprofiel : een HD-profiel heeft dikkere flenzen en lijf. Dit profiel is speciaal voor kolommen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hd")
        self.add_option("hea", "HEA", "Meest voorkomende breedflensprofiel (een profiel met brede evenwijdige flenzen).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hea")
        self.add_option("heb", "HEB", "Meest voorkomende breedflensprofiel (een profiel met brede evenwijdige flenzen). Het HEB-profiel heeft meer draagkracht dan het HEA-profiel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/heb")
        self.add_option("hem", "HEM", "Breedflensprofiel : een HEM-profiel heeft dikkere flenzen en lijf dan HEA- en HEB-profielen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hem")
        self.add_option("hp-bulbstaal", "HP (bulbstaal)", "Een massief profiel : Hollandprofiel (afgekort HP).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hp-bulbstaal")
        self.add_option("ipe", "IPE", "Een IPE-profiel (I Profiel Europees) heeft betrekkelijk korte, evenwijdige flenzen met een constante dikte.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/ipe")
        self.add_option("ipn", "IPN", "Een IPN-profiel (I Normaal Profiel, ook wel INP genoemd) heeft iets schuinere flenzen dan een IPE-profiel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/ipn")
        self.add_option("upe", "UPE", "U-vormig profiel. Een UPE-profiel heeft rechte flenzen die overal even dik zijn en dikker zijn dan het lijf.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/upe")
        self.add_option("upn", "UPN", "Het meest gebruikte U-vormig profiel. Een UPN-profiel (U Normaal Profiel, ook wel UNP genoemd) heeft schuine flenzen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/upn")
