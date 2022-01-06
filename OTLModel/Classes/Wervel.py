from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wervel(LinkendElement):
    """Een wervel is een debietsbeperkend element dat zich tussen 2 kamers of tussen een kamer en een leiding bevindt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wervel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.peil = KwantWrdInMeterTAW()
        """Dit is het niveau in meter-TAW van de inlaat van het wervelventiel."""
        self.peil.naam = "peil"
        self.peil.label = "peil"
        self.peil.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wervel.peil"
        self.peil.definition = "Dit is het niveau in meter-TAW van de inlaat van het wervelventiel."
        self.peil.constraints = ""
        self.peil.usagenote = ""
        self.peil.deprecated_version = ""
