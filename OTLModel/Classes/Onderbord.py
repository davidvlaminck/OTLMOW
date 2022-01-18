# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderbord(RetroreflecterendVerkeersbord, AttributeInfo):
    """Een bord met een verkeersteken dat als toevoeging onder een verkeersbord is gehangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        RetroreflecterendVerkeersbord.__init__(self)
