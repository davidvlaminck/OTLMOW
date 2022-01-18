# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class PutRelatie(AIMObject, AttributeInfo):
    """Abstracte om de relaties van de verschillende soorten putten te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
