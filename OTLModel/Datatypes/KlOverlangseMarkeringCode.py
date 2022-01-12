# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverlangseMarkeringCode(Keuzelijst):
    """Codes van de overlangse markering."""

    def __init__(self):
        super().__init__(naam="KlOverlangseMarkeringCode",
                         label="Overlangse markering code",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverlangseMarkeringCode",
                         definition="Codes van de overlangse markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverlangseMarkeringCode")

        self.add_option("BAD-0.20", "BAD 0.20", "Doorlopende overlangse bushalte aslijn markering (0.2 meter breedte).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/BAD-0.20")
        self.add_option("BAD-0.30", "BAD 0.30", "Doorlopende overlangse bushalte aslijn markering (0.3 meter breedte).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/BAD-0.30")
        self.add_option("BAO-0.30-x-2.50-(1)", "BAO 0.30 x 2.50 (1)", "Onderbroken overlangse bushalte aslijn markering (0.3 meter breedte en 2.5 meter lengte).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/BAO-0.30-x-2.50-(1)")
        self.add_option("FAD-0.15", "FAD 0.15", "Doorlopende overlangse fietspad aslijn markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FAD-0.15")
        self.add_option("FAO-0.15-x-1.25-(1.25)", "FAO 0.15 x 1.25 (1.25)", "Onderbroken overlangse fietspad aslijn markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FAO-0.15-x-1.25-(1.25)")
        self.add_option("FAO-0.15-x-1.25-(3.25)", "FAO 0.15 x 1.25 (3.25)", "Onderbroken overlangse fietspad aslijn markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FAO-0.15-x-1.25-(3.25)")
        self.add_option("FRO-0.15-x-1.25-(1.25)", "FRO 0.15 x 1.25 (1.25)", "Onderbroken overlangse fietspad randlijn markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FRO-0.15-x-1.25-(1.25)")
        self.add_option("FRO-0.15-x-1.25-(3.75)", "FRO 0.15 x 1.25 (3.75)", "Onderbroken overlangse fietspad randlijn markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FRO-0.15-x-1.25-(3.75)")
        self.add_option("PRD-0.10", "PRD 0.10", "Doorlopende overlangse randlijn parkeerstrook markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/PRD-0.10")
        self.add_option("RAD-0.15", "RAD 0.15", "Doorlopende overlange markering (0.15 meter breedte).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAD-0.15")
        self.add_option("RAD-0.20", "RAD 0.20", "Doorlopende overlange markering (0.2 meter breedte).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAD-0.20")
        self.add_option("RAO-0.15-x-1.00-(1.5)", "RAO 0.15 x 1.00 (1.5)", "Onderbroken overlangse aslijn markering (1.5 meter tussenruimte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.15-x-1.00-(1.5)")
        self.add_option("RAO-0.15-x-2.50-(10)", "RAO 0.15 x 2.50 (10)", "Onderbroken overlangse aslijn markering (10 meter tussenruimte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.15-x-2.50-(10)")
        self.add_option("RAO-0.20-x-1.00-(1.5)", "RAO 0.20 x 1.00 (1.5)", "Onderbroken overlangse aslijn markering (1.5 meter tussenruimte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.20-x-1.00-(1.5)")
        self.add_option("RAO-0.20-x-2.50-(10)", "RAO 0.20 x 2.50 (10)", "Onderbroken overlangse aslijn markering (10 meter tussenruimte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.20-x-2.50-(10)")
        self.add_option("RAO-0.30-x-1.00-(1.5)", "RAO 0.30 x 1.00 (1.5)", "Onderbroken overlangse aslijn markering (1.5 meter tussenruimte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.30-x-1.00-(1.5)")
        self.add_option("RRD-0.15", "RRD 0.15", "Doorlopende overlangse randlijn markering (0.15 meter breedte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.15")
        self.add_option("RRD-0.20", "RRD 0.20", "Doorlopende overlangse randlijn markering (0.20 meter breedte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.20")
        self.add_option("RRD-0.25", "RRD 0.25", "Doorlopende overlangse randlijn markering (0.25 meter breedte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.25")
        self.add_option("RRD-0.30", "RRD 0.30", "Doorlopende overlangse randlijn markering (0.30 meter breedte)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.30")
        self.add_option("SAO-0.20-x-10-(2.5)", "SAO 0.20 x 10 (2.5)", "Onderbroken overlangse aslijn spitsstrook markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/SAO-0.20-x-10-(2.5)")
