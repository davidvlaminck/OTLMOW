# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class SlagboomarmVerlichting(AIMObject, AttributeInfo):
    """Verlichting bevestigd aan de slagboomarm om de zichtbaarheid van die arm te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
