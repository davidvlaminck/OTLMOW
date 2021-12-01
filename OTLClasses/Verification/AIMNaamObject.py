from abc import ABC, abstractmethod

from ModelGenerator.BaseClasses.StringField import StringField


# inherit from ABC to create abstract class
class AIMNaamObject(ABC):
    """Abstracte als de basisklasse voor elk OTL object dat benoemd wordt met een mensleesbare identificator."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject"
    naam = StringField()
    """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

