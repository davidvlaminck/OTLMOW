# coding=utf-8
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hanger(ConstructiefObject):
    """Een kabel of een stalen staaf die het brugdek ophangt aan de boog. Deze brengt de trekkrachten van het brugdek over naar de boog."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
