# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.SoortenrijkSchraalGraslandGraslandfase5 import SoortenrijkSchraalGraslandGraslandfase5


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dwerghavergrasland(SoortenrijkSchraalGraslandGraslandfase5, AttributeInfo):
    """G5b - vroege haver, klein vogelpootje, zilverhaver,
klein tasjeskruid, dwergviltkruid, eekhoorngras
en zandblauwtje, veldereprijs , hazenpootje,
eenjarige hardbloem, rode schijnspurrie,
akkerviooltje, zandmuur, reigersbek, spurrie,
straatgras, zandraket, vroegeling, kleine
leeuwenklauw, zachte ooievaarsbek, klein
streepzaad, gewoon langbaardgras,zandhoornbloem, slofhak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dwerghavergrasland'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        SoortenrijkSchraalGraslandGraslandfase5.__init__(self)
