from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftBeheer(DirectioneleRelatie):
    """De relatie geeft aan dat een onderdeel wordt beheerd. Het beheer object bevat de nodige beheer eigenschappen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
