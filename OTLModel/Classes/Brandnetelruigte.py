# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Ruigte import Ruigte


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandnetelruigte(Ruigte, AttributeInfo):
    """R3 - dominante bedekking van grote brandnetel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandnetelruigte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Ruigte.__init__(self)
