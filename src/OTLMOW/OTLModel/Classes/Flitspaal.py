# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitspaal(AIMNaamObject):
    """Buiteninstallatie waarin een flitscamera geplaatst kan worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
