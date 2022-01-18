# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Proef(AIMObject, AttributeInfo):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties alle proeven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Proef'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
