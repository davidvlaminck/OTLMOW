# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.SoortenrijkSchraalGraslandGraslandfase5 import SoortenrijkSchraalGraslandGraslandfase5


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kalkgrasland(SoortenrijkSchraalGraslandGraslandfase5, AttributeInfo):
    """G5c - blauwgras, bergdravik, duifkruid, grote centaurie, ruige scheefkelk, geel zonneroosje, kleine pimpernel, kalkwalstro, gevinde kortsteel, aarddistel, smal fakkelgras, driedistel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kalkgrasland'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        SoortenrijkSchraalGraslandGraslandfase5.__init__(self)
