# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.DNB import DNB


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBHoogspanning(DNB, AttributeInfo):
    """Aansluiting op het hoogspanningsnet van de distributienetbeheerder."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBHoogspanning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        DNB.__init__(self)
