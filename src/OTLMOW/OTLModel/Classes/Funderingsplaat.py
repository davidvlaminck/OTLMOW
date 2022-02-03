# coding=utf-8
from OTLMOW.OTLModel.Classes.Betonfundering import Betonfundering
from OTLMOW.OTLModel.Classes.KlassiekeFundering import KlassiekeFundering


# Generated with OTLClassCreator. To modify: extend, do not edit
class Funderingsplaat(Betonfundering, KlassiekeFundering):
    """Fundering die minstens het volledige grondvlak van het gefundeerd object omvat maar met een beperkte hoogte voor de fundering van een constructie die stabiliteit haalt uit haar eigen gewicht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Betonfundering.__init__(self)
        KlassiekeFundering.__init__(self)
