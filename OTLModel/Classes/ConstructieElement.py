# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class ConstructieElement(AIMObject):
    """Abstracte voor de verschillende constructie elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
