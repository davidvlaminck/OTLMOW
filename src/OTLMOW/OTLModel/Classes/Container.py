# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Inloopbehuizing import Inloopbehuizing


# Generated with OTLClassCreator. To modify: extend, do not edit
class Container(Inloopbehuizing):
    """Een verplaatsbare behuizing voor het beschermen van technieken en materialen waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Container'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
