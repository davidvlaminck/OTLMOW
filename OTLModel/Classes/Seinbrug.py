from OTLModel.Classes.VRIDraagconstructie import VRIDraagconstructie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSeinbrugRijrichting import KlSeinbrugRijrichting
from OTLModel.Datatypes.KlSeinbrugType import KlSeinbrugType
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Seinbrug(VRIDraagconstructie):
    """Metalen constructie bestaande uit twee of meer verticale steunen met voetplaat en uit een enkele of een dubbel uitgevoerde horizontale dwarsverbinding, allen kokervormig met rechthoekige doorsnede. Ook wel portiek of portaal genoemd."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalLadders = DecimalFloatField(naam="aantalLadders",
                                               label="aantal ladders",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.aantalLadders",
                                               definition="Het aantal ladders waarmee de seinbrug toegankelijk is.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Het aantal ladders waarmee de seinbrug toegankelijk is."""

        self.aantalSteunen = DecimalFloatField(naam="aantalSteunen",
                                               label="aantal steunen",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.aantalSteunen",
                                               definition="Het aantal steunen waarmee de seinbrug gedragen wordt. ",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Het aantal steunen waarmee de seinbrug gedragen wordt. """

        self.berekeningsnota = DtcDocument()
        """Een bijlage met de berekeningsnota voor de seinbrug."""
        self.berekeningsnota.naam = "berekeningsnota"
        self.berekeningsnota.label = "berekeningsnota"
        self.berekeningsnota.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.berekeningsnota"
        self.berekeningsnota.definition = "Een bijlage met de berekeningsnota voor de seinbrug."
        self.berekeningsnota.constraints = ""
        self.berekeningsnota.usagenote = ""
        self.berekeningsnota.deprecated_version = ""

        self.controlemetingEBS = DtcDocument()
        """Een bijlage met het verslag van de controlemeting uitgevoerd door het Expertisecentrum Beton en Staal."""
        self.controlemetingEBS.naam = "controlemetingEBS"
        self.controlemetingEBS.label = "controlemeting EBS"
        self.controlemetingEBS.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.controlemetingEBS"
        self.controlemetingEBS.definition = "Een bijlage met het verslag van de controlemeting uitgevoerd door het Expertisecentrum Beton en Staal."
        self.controlemetingEBS.constraints = ""
        self.controlemetingEBS.usagenote = ""
        self.controlemetingEBS.deprecated_version = ""

        self.heeftLooproosters = BooleanField(naam="heeftLooproosters",
                                              label="heeft looproosters",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.heeftLooproosters",
                                              definition="Geeft aan of de seinbrug is uitgerust met looproosters.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Geeft aan of de seinbrug is uitgerust met looproosters."""

        self.hoogteVerticaleSteun = KwantWrdInMeter()
        """Verticale afstand (in meter) tussen de bovenkant van het wegdek en de bovenkant van het hoogste constructiedeel van de seinbrug."""
        self.hoogteVerticaleSteun.naam = "hoogteVerticaleSteun"
        self.hoogteVerticaleSteun.label = "hoogte verticale steun"
        self.hoogteVerticaleSteun.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.hoogteVerticaleSteun"
        self.hoogteVerticaleSteun.definition = "Verticale afstand (in meter) tussen de bovenkant van het wegdek en de bovenkant van het hoogste constructiedeel van de seinbrug."
        self.hoogteVerticaleSteun.constraints = ""
        self.hoogteVerticaleSteun.usagenote = ""
        self.hoogteVerticaleSteun.deprecated_version = ""

        self.overspanning = KwantWrdInMeter()
        """De afstand tussen de twee steunpunten van de seinbrug."""
        self.overspanning.naam = "overspanning"
        self.overspanning.label = "overspanning"
        self.overspanning.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.overspanning"
        self.overspanning.definition = "De afstand tussen de twee steunpunten van de seinbrug."
        self.overspanning.constraints = ""
        self.overspanning.usagenote = ""
        self.overspanning.deprecated_version = ""

        self.rijrichting = KeuzelijstField(naam="rijrichting",
                                           label="rijrichting",
                                           lijst=KlSeinbrugRijrichting(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.rijrichting",
                                           definition="Geeft aan of de seinbrug één of beide rijrichtingen overspant.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of de seinbrug één of beide rijrichtingen overspant."""

        self.technischeFiche = DtcDocument()
        """Een bijlage waarin de detailtekeningen van de seinbrug."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.technischeFiche"
        self.technischeFiche.definition = "Een bijlage waarin de detailtekeningen van de seinbrug."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlSeinbrugType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.type",
                                    definition="Het type van de seinbrug volgens de aard van de constructie.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de seinbrug volgens de aard van de constructie."""

        self.vrijeHoogte = KwantWrdInMeter()
        """De verticale afstand (in meter) tussen de bovenkant van het wegdek en de onderkant van het laagste, daarboven gelegen constructiedeel van de seinbrug."""
        self.vrijeHoogte.naam = "vrijeHoogte"
        self.vrijeHoogte.label = "vrije hoogte"
        self.vrijeHoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.vrijeHoogte"
        self.vrijeHoogte.definition = "De verticale afstand (in meter) tussen de bovenkant van het wegdek en de onderkant van het laagste, daarboven gelegen constructiedeel van de seinbrug."
        self.vrijeHoogte.constraints = ""
        self.vrijeHoogte.usagenote = ""
        self.vrijeHoogte.deprecated_version = ""
