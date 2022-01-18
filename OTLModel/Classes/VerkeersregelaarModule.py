# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersregelaarModule(AIMNaamObject, AttributeInfo):
    """Abstracte voor de verschillende modules waaruit een verkeersregelaar opgebouwd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerkeersregelaarModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)
