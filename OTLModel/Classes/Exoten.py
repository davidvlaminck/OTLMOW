# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen


# Generated with OTLClassCreator. To modify: extend, do not edit
class Exoten(BegroeidVoorkomen, AttributeInfo):
    """Exoten, in deze context, zijn planten die zich hebben gevestigd in België terwijl ze oorspronkelijk niet in België voorkwamen. Ze verdringen bovendien inheemse soorten uit hun normale groeiplaats."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Exoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        BegroeidVoorkomen.__init__(self)
