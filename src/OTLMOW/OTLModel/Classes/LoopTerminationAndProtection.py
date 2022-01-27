# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class LoopTerminationAndProtection(AIMNaamObject):
    """(Groene) aansluitblok met afsluitimpedantie en beveiliging voor de inductieve lussen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LoopTerminationAndProtection'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
