# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handwiel(AIMObject, AttributeInfo):
    """Een handwiel kan worden gebruikt voor het openen of sluiten van een afsluiter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handwiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
