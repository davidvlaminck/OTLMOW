# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugdek(AIMNaamObject):
    """Dragende structuur die kan bestaan uit platen, balken,... Deze kan uitgevoerd worden in verschillende materialen (beton, staal, kunststof, hout)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
