# coding=utf-8
from OTLModel.Classes.Brandvoorziening import Brandvoorziening


# Generated with OTLClassCreator. To modify: extend, do not edit
class VulpuntBrandweer(Brandvoorziening):
    """Klep in de brandleiding waar een vulwagen van de brandweer het debiet van de brandleiding kan verhogen door water toe voegen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VulpuntBrandweer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
