# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LigtOp(DirectioneleRelatie, AttributeInfo):
    """Deze relatie geeft aan dat 2 onderdelen direct fysiek op elkaar liggen. Deze relatie heeft een richting en gaat van het bovenste naar het onderste onderdeel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        DirectioneleRelatie.__init__(self)
