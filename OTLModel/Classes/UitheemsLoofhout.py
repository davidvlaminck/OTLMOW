# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.OpgaandeHoutigeVegetatie import OpgaandeHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class UitheemsLoofhout(OpgaandeHoutigeVegetatie):
    """H4 - Jonge aanplant met dominantie van allerlei loofhout op niet-bosbodems, incl. exoten (Robinia, populier, vederesdoorn, Amerikaanse eik, Amerikaanse vogelkers) eventueel met bijmenging van struweelsoorten (S3 tot S5)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UitheemsLoofhout'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
