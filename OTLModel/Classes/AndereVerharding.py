# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.ArtificieleLaag import ArtificieleLaag


# Generated with OTLClassCreator. To modify: extend, do not edit
class AndereVerharding(ArtificieleLaag, AttributeInfo):
    """Abstracte voor de andere verhardingen, met een ander fysiek voorkomen van het aardoppervlak dat niet vegetatief is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereVerharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        ArtificieleLaag.__init__(self)
        AttributeInfo.__init__(self)
