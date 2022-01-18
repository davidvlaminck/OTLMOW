# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleiding(AIMObject, AttributeInfo):
    """Abstracte om de gerelateerde objecten onder 1 noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
