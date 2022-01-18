# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Struweel import Struweel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Doornstruweel(Struweel, AttributeInfo):
    """S3
 - meidoorn spp, sleedoorn en rozen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doornstruweel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Struweel.__init__(self)
