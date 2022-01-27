# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoedtAangestuurd(DirectioneleRelatie):
    """Deze relatie wordt enkel gelegd naar objecttypes die typisch een groot vermogen vereisen en onder spanning komen nadat het voedend element aangestuurd is om die spanning door te sturen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
