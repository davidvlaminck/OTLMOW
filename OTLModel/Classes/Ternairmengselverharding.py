# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereVerharding import AndereVerharding


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ternairmengselverharding(AndereVerharding, AttributeInfo):
    """Een verharding van gebonden mengsel van grof brekerzand van natuurlijke stenen, eventueel gemengd met brekerzand van hoogovenslakken en steenslag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ternairmengselverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereVerharding.__init__(self)
        AttributeInfo.__init__(self)
