# coding=utf-8
from OTLMOW.OTLModel.Classes.Brugligger import Brugligger


# Generated with OTLClassCreator. To modify: extend, do not edit
class Langsligger(Brugligger):
    """Balk volgens de lengterichting van de brug, waarop de eigenlijke rijvloer direct komt te dragen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Langsligger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
