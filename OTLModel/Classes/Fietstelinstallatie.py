# coding=utf-8
from OTLModel.Classes.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fietstelinstallatie(NaampadObject):
    """Groepering van onderdelen die samen een installatie vormen voor het verzamelen van telgegevens over passerende fietsers en in sommige installaties het tonenvan de gegevens."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fietstelinstallatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
