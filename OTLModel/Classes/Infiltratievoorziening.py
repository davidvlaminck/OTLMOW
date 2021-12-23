from OTLModel.Classes.Put import Put
from OTLModel.Classes.PutRelatie import PutRelatie


# Generated with OTLClassCreator
class Infiltratievoorziening(Put, PutRelatie):
    """Voorziening voor infiltratie van onvervuild water."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Infiltratievoorziening"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)
