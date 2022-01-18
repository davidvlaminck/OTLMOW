# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.Geleiding import Geleiding


# Generated with OTLClassCreator. To modify: extend, do not edit
class ComplexeGeleiding(Geleiding, AttributeInfo):
    """Een Abstracte die de SluitAanOp relatie mogelijk maakt voor de samenstellende onderdelen van een complexere geleiding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AttributeInfo.__init__(self)
        Geleiding.__init__(self)
