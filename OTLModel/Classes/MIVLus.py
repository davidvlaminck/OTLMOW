from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlMIVLusUitslijprichting import KlMIVLusUitslijprichting
from OTLModel.Datatypes.KlMIVLusZichtbaarheid import KlMIVLusZichtbaarheid


# Generated with OTLClassCreator
class MIVLus(AIMNaamObject):
    """Meten in Vlaanderen : inductieve lus, ingeslepen in het wegdek."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.meetrapport = DtcDocument()
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        self.meetrapport.naam = "meetrapport"
        self.meetrapport.label = "meetrapport"
        self.meetrapport.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.meetrapport"
        self.meetrapport.definition = "De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."
        self.meetrapport.constraints = ""
        self.meetrapport.usagenote = "Bestanden van het type pdf."
        self.meetrapport.deprecated_version = ""

        self.uitslijprichting = KeuzelijstField(naam="uitslijprichting",
                                                label="uitslijprichting",
                                                lijst=KlMIVLusUitslijprichting(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.uitslijprichting",
                                                definition="De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting."""

        self.zichtbaarheid = KeuzelijstField(naam="zichtbaarheid",
                                             label="zichtbaarheid",
                                             lijst=KlMIVLusZichtbaarheid(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.zichtbaarheid",
                                             definition="Is dus lus zichtbaar in het wegdek of bedekt door een toplaag.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Is dus lus zichtbaar in het wegdek of bedekt door een toplaag."""
