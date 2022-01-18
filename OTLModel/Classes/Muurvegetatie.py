# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VegetatieElement import VegetatieElement


# Generated with OTLClassCreator. To modify: extend, do not edit
class Muurvegetatie(VegetatieElement, AttributeInfo):
    """Muurvegetaties zijn gebonden aan door de mens gecreëerde stenige, doorgaans steile tot verticale standplaatsen. Voorbeelden zijn kerkhofmuren, stadswallen, ruïnes, kademuren, oude forten en bunkers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurvegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        VegetatieElement.__init__(self)
