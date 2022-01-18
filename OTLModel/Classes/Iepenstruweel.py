# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.OpgaandeHoutigeVegetatie import OpgaandeHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Iepenstruweel(OpgaandeHoutigeVegetatie, AttributeInfo):
    """H2 - Houtige begroeiing in holle wegen van de leemstreek met gladde iep, ruwe iep, meidoorn spp., gewone es, gewone vlier, maarts viooltje, vogelmelk, aalbes, gevlekte aronskelk, speenkruid, vingerhelmbloem, grote keverorchis, klimop, klimopereprijs, look-zonder-look."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Iepenstruweel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        OpgaandeHoutigeVegetatie.__init__(self)
