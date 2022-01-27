# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Kamer import Kamer


# Generated with OTLClassCreator. To modify: extend, do not edit
class Reservoir(Kamer):
    """Een reservoir is een complexe kamer die verschillende niveaus en gekoppelde oppervlaktes kan hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Reservoir'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
