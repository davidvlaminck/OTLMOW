from abc import abstractmethod
from OTLModel.Classes.ArtificieleLaag import ArtificieleLaag


# Generated with OTLClassCreator
class AndereVerharding(ArtificieleLaag):
    """Abstracte voor de andere verhardingen, met een ander fysiek voorkomen van het aardoppervlak dat niet vegetatief is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereVerharding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
