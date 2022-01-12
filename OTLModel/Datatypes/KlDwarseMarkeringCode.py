# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringCode(Keuzelijst):
    """Codes van de dwarse markering."""

    def __init__(self):
        super().__init__(naam="KlDwarseMarkeringCode",
                         label="Dwarse markering code",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringCode",
                         definition="Codes van de dwarse markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringCode")

        self.add_option("DAMBRD", "DAMBRD", "Dambord", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DAMBRD")
        self.add_option("DREMPEL-1.2", "DREMPEL 1.2", "Verkeersdrempel markering", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DREMPEL-1.2")
        self.add_option("DRH-fiets-(0.3)", "DRH fiets (0.3)", "Driehoek fiets", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-fiets-(0.3)")
        self.add_option("DRH-std-(0.7)", "DRH std (0.7)", "Driehoek standaard", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-std-(0.7)")
        self.add_option("FLV", "FLV", "Verbindingsmarkering voor fietsers.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FLV")
        self.add_option("FOP", "FOP", "Fietsoversteekplaats met blokken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FOP")
        self.add_option("PARKEER", "PARKEER", "Parkeerstrook", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/PARKEER")
        self.add_option("RIBBELSTROOK---AFREMMINGSSTREPEN", "RIBBELSTROOK - AFREMMINGSSTREPEN", "Afremmingsstreep", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/RIBBELSTROOK---AFREMMINGSSTREPEN")
        self.add_option("STOPSTRP", "STOPSTRP", "Code voor de stopstreep", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP")
        self.add_option("STOPSTRP-OFOS", "STOPSTRP-OFOS", "Code voor de stopstreep OFOS", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP-OFOS")
        self.add_option("VOP-(3)", "VOP (3)", "Voetgangers-oversteekplaats (3 meter)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(3)")
        self.add_option("VOP-(4)", "VOP (4)", "Voetgangers-oversteekplaats (4 meter)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(4)")
        self.add_option("VOP-(var)", "VOP (var)", "Voetgangers-oversteekplaats (te meten)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(var)")
        self.add_option("VVA-0.4-(0.6)", "VVA 0.4 (0.6)", "Verdrijvingsvlak (40 % opp. v.h. vlak)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-0.4-(0.6)")
        self.add_option("VVA-1-(2)", "VVA 1 (2)", "Verdrijvingsvlak (33 % opp. v.h. vlak)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-1-(2)")
