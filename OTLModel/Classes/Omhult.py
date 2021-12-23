from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator
class Omhult(DirectioneleRelatie):
    """Deze relatie geeft aan dat het ene onderdeel het andere omhult. Deze relatie heeft een richting en gaat van het omhullende onderdeel naar het onderdeel dat omhult wordt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
