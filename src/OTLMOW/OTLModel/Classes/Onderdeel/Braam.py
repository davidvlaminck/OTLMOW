# coding=utf-8
from OTLMOW.OTLModel.Classes.Onderdeel.Struweel import Struweel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Braam(Struweel):
    """S4 - braam spp (inclusief framboos)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Braam'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
