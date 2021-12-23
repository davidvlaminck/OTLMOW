from OTLModel.Verification.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere


class Laagspanningsbord(AIMNaamObject):
    """Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn.
    Omvat onder andere automaten,klemmenblokken,... """
    def __init__(self):
        super().__init__()
        self.aansluitvermogen = KwantWrdInAmpere()
        """Het vermogen van het laagspanningsbord."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""