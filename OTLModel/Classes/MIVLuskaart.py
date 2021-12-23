from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class MIVLuskaart(AIMNaamObject):
    """Meten in Vlaanderen : kaart in LVE- of SAT- rack met de analoge circuits voor de lussen en analoog/digitaal conversie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.lussenMeetrapport = DtcDocument()
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        self.lussenMeetrapport.naam = "lussenMeetrapport"
        self.lussenMeetrapport.label = "lussen meetrapport"
        self.lussenMeetrapport.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart.lussenMeetrapport"
        self.lussenMeetrapport.definition = "De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."
        self.lussenMeetrapport.constraints = ""
        self.lussenMeetrapport.usagenote = "Bestanden van het type pdf."
        self.lussenMeetrapport.deprecated_version = ""
