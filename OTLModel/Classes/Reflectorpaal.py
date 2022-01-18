# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Bebakening import Bebakening


# Generated with OTLClassCreator. To modify: extend, do not edit
class Reflectorpaal(Bebakening, AttributeInfo):
    """Een kunststoffen paal met reflector om het verkeer te geleiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Reflectorpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Bebakening.__init__(self)
