# coding=utf-8
from OTLMOW.OTLModel.Classes.ConstructieElement import ConstructieElement


# Generated with OTLClassCreator. To modify: extend, do not edit
class ConstructiefObject(ConstructieElement):
    """Een bundeling van alle constructieve installaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructiefObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
