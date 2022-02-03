# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlEcoLooprichelType import KlEcoLooprichelType
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduiker(AIMObject, VlakGeometrie):
    """Buis- of tunnelvormige doorgang voor water onder een weg, die is voorzien van een oeverstrook of van looprichels zodat kleinere diersoorten beschermd voor het verkeer kunnen doorsteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._typeLooprichel = OTLAttribuut(field=KlEcoLooprichelType,
                                            naam='typeLooprichel',
                                            label='type looprichel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker.typeLooprichel',
                                            definition='Type van looprichel in de ecoduiker.',
                                            owner=self)

    @property
    def typeLooprichel(self):
        """Type van looprichel in de ecoduiker."""
        return self._typeLooprichel.waarde

    @typeLooprichel.setter
    def typeLooprichel(self, value):
        self._typeLooprichel.set_waarde(value, owner=self)
