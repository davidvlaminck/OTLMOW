# coding=utf-8
from OTLMOW.OTLModel.Classes.Brugligger import Brugligger


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoofdligger(Brugligger):
    """Hoofdconstructiedeel van een brug, aan weerskanten van de te overspannen rivier of weg opgelegd en onderling tot een stijf geheel door zogenaamd windkruizen verbonden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hoofdligger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
