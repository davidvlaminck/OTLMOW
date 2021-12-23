from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator
class HeeftNetwerktoegang(DirectioneleRelatie):
    """Koppelt de toegang zoals gekend in Kabelnet aan het fysiek object dat daarbij hoort."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerktoegang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
