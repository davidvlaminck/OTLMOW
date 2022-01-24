# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Grasland import Grasland


# Generated with OTLClassCreator. To modify: extend, do not edit
class DominantGraslandfase2(Grasland):
    """G2 - Meer dan 50% van de oppervlakte ingenomen door één niet sterk glanzende grassoort:gestreepte witbol, grote vossenstaart of glanshaver, + grassen en kruiden uit G0 en G1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DominantGraslandfase2'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
