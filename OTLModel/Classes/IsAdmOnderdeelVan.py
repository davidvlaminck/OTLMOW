# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsAdmOnderdeelVan(DirectioneleRelatie, AttributeInfo):
    """Deze relatie geeft aan dat een onderdeel louter met een administratieve functie toebehoort aan de collectie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsAdmOnderdeelVan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        DirectioneleRelatie.__init__(self)
