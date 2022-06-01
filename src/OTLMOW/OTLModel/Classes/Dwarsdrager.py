# coding=utf-8
from OTLMOW.OTLModel.Classes.Brugligger import Brugligger


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dwarsdrager(Brugligger):
    """Dragende dwarsbalk tussen de hoofdliggers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Dwarsdrager'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
