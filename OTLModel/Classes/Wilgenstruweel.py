# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.OpgaandeHoutigeVegetatie import OpgaandeHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wilgenstruweel(OpgaandeHoutigeVegetatie, AttributeInfo):
    """H1 - wilgensoorten, sporkehout, gewone vlier, braam spp., brede stekelvaren, grote brandnetel, hondsdraf, kleefkruid, pitrus."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wilgenstruweel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        OpgaandeHoutigeVegetatie.__init__(self)
