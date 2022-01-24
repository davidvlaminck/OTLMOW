# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Struweel import Struweel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Doornstruweel(Struweel):
    """Een plank of paneel om een grond- en/of waterkerende constructie, verticaal in de grond, te maken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doornstruweel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
