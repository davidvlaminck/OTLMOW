# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsNetwerkECC(DirectioneleRelatie):
    """Deze relatie geeft aan hoe afgeschermde netwerkelementen bereikt kunnen worden vanuit het gewone netwerk. De relatie vertrekt steeds in het controlerende netwerkelement."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsNetwerkECC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
