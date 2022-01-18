# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlEcoLooprichelType import KlEcoLooprichelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduiker(AIMObject, AttributeInfo):
    """Buis- of tunnelvormige doorgang voor water onder een weg, die is voorzien van een oeverstrook of van looprichels zodat kleinere diersoorten beschermd voor het verkeer kunnen doorsteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._typeLooprichel = OTLAttribuut(field=KlEcoLooprichelType,
                                            naam='typeLooprichel',
                                            label='type looprichel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker.typeLooprichel',
                                            definition='Type van looprichel in de ecoduiker.')

    @property
    def typeLooprichel(self):
        """Type van looprichel in de ecoduiker."""
        return self._typeLooprichel.waarde

    @typeLooprichel.setter
    def typeLooprichel(self, value):
        self._typeLooprichel.set_waarde(value, owner=self)
