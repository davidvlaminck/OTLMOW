# coding=utf-8
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Boog(ConstructiefObject):
    """Een gebogen overspanning (boven een opening), tussen twee steunpunten en ter ondersteuning van een brug, waarbij de druk (ook) zijdelings wordt afgevoerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Boog'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
