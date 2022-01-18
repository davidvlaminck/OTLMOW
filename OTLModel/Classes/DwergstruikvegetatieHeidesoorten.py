# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Struweel import Struweel


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwergstruikvegetatieHeidesoorten(Struweel, AttributeInfo):
    """S1 - struikheide, dopheide, blauwe bosbes,stekelbrem, kruipbrem."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwergstruikvegetatieHeidesoorten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Struweel.__init__(self)
