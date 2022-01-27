# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.OpgaandeHoutigeVegetatie import OpgaandeHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Naaldhout(OpgaandeHoutigeVegetatie):
    """H5 - Naaldhoutbestanden van allerlei aard: van mono-specifiek of dominant tot gevarieerd met o.a. zwarte den, grove den, spar spp., lork, Douglas en ev. struweelsoorten (soorten uit S1, S2, S4, S5)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Naaldhout'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
