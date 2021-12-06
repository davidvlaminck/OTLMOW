from OTLClasses.Verification.AIMNaamObject import AIMNaamObject
from OTLClasses.Verification.KwantWrdInAmpere import KwantWrdInAmpere


class Laagspanningsbord(AIMNaamObject):
    """Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn.
    Omvat onder andere automaten,klemmenblokken,... """
    def __init__(self):
        pass

    aansluitvermogen = KwantWrdInAmpere()
    """Het vermogen van het laagspanningsbord."""

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord"
