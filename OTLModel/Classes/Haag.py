# coding=utf-8
from OTLModel.Classes.HoutigeVegetatie import HoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Haag(HoutigeVegetatie):
    """Hagen zijn smalle lijnvormige elementen bestaande uit houtige soorten die geschoren kunnen worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Haag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
