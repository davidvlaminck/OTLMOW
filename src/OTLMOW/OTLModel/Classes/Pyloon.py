# coding=utf-8
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pyloon(ConstructiefObject):
    """Een pyloon is een taps toelopende hoge constructie, als drager van kabels e.d. (bv. een hoogspanningmast of een mast van een brug)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pyloon'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
