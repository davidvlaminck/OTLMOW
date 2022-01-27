# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.OpgaandeHoutigeVegetatie import OpgaandeHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Loofhout(OpgaandeHoutigeVegetatie):
    """H3 - Vegetaties op gerijpte, mesofiele tot droge bosbodems, gedomineerd door inheemse loofbomen. Boomlaag van mono-specifiek of dominant tot zeer gevarieerd met o.a.: beuk, zomereik, wintereik gewone es, haagbeuk, esdoorn, berk spp., hazelaar, zoete kers, trilpopulier. Mogelijke bijmenging (maar nooit dominant) met zwarte els, grauwe els, wilgen spp., sporkehout, en struweelsoorten (zie S1 tot S5). Kruidlaag: van afwezig tot zeer rijk met oude bosplanten (zie bijlage 3)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loofhout'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
