# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecovallei(AIMObject, AttributeInfo):
    """Een vallei onder de verkeersbrug waar het landschap gewoon onderdoor loopt en minimaal wordt verstoord."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecovallei'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
