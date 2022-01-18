# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereLaag import AndereLaag


# Generated with OTLClassCreator. To modify: extend, do not edit
class Noppendrainage(AndereLaag, AttributeInfo):
    """Een noppendrainveld zorgt voor een verticale afwatering van het overtollige water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noppendrainage'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        AttributeInfo.__init__(self)
