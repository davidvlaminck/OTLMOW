# coding=utf-8
from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOverstortMateriaalDrempel import KlOverstortMateriaalDrempel
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overstort(LinkendElement):
    """Een overstort is een drempel tussen twee kamers waar water vanaf een bepaald peil van de ene naar de andere kamer kan stromen. Tussen twee kamers kunnen een of meerdere overstorten voorkomen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.drempellengte = KwantWrdInMillimeter()
        """Drempellengte of breedte van de overstort. Deze wordt gemeten aan de kortste zijdevan de drempel."""
        self.drempellengte.naam = "drempellengte"
        self.drempellengte.label = "breedte"
        self.drempellengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.drempellengte"
        self.drempellengte.definition = "Drempellengte of breedte van de overstort. Deze wordt gemeten aan de kortste zijdevan de drempel."
        self.drempellengte.constraints = ""
        self.drempellengte.usagenote = ""
        self.drempellengte.deprecated_version = ""

        self.materiaalDrempel = KeuzelijstField(naam="materiaalDrempel",
                                                label="materiaal drempel",
                                                lijst=KlOverstortMateriaalDrempel(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.materiaalDrempel",
                                                definition="Het gebruikte materiaal voor het vervaardigen van de overstort (drempel).",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Het gebruikte materiaal voor het vervaardigen van de overstort (drempel)."""

        self.peil = KwantWrdInMeterTAW()
        """Drempelpeil van de overstort. Uitgedrukt in meter-TAW gemeten in het midden van de drempel."""
        self.peil.naam = "peil"
        self.peil.label = "peil"
        self.peil.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.peil"
        self.peil.definition = "Drempelpeil van de overstort. Uitgedrukt in meter-TAW gemeten in het midden van de drempel."
        self.peil.constraints = ""
        self.peil.usagenote = ""
        self.peil.deprecated_version = ""

        self.vrijeHoogte = KwantWrdInMeter()
        """De vrije hoogte tussen de overstortdrempel en het plafond van deconstructie ter hoogte van de drempel. Voor drempels in leidingen wordende vrije hoogte voor de databank genomen tussen de drempel en debinnenbovenkant buis. Indien er geen sprake is van een vrije hoogte (vbdrempels in grachten) wordt dit niet ingevuld."""
        self.vrijeHoogte.naam = "vrijeHoogte"
        self.vrijeHoogte.label = "vrije hoogte"
        self.vrijeHoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.vrijeHoogte"
        self.vrijeHoogte.definition = "De vrije hoogte tussen de overstortdrempel en het plafond van deconstructie ter hoogte van de drempel. Voor drempels in leidingen wordende vrije hoogte voor de databank genomen tussen de drempel en debinnenbovenkant buis. Indien er geen sprake is van een vrije hoogte (vbdrempels in grachten) wordt dit niet ingevuld."
        self.vrijeHoogte.constraints = ""
        self.vrijeHoogte.usagenote = ""
        self.vrijeHoogte.deprecated_version = ""
