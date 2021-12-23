from abc import abstractmethod
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator
class Straatmeubilair(Signalisatie, AIMObject):
    """Abstracte bedoeld om het straatmeubilair onder 1 noemer te houden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Signalisatie.__init__(self)
        AIMObject.__init__(self)
