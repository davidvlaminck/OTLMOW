# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen


# Generated with OTLClassCreator. To modify: extend, do not edit
class Exoten(BegroeidVoorkomen):
    """Exoten, in deze context, zijn planten die zich hebben gevestigd in België terwijl ze oorspronkelijk niet in België voorkwamen. Ze verdringen bovendien inheemse soorten uit hun normale groeiplaats."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Exoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.1.0'

    def __init__(self):
        super().__init__()
