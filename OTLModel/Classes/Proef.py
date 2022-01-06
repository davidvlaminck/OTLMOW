# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Proef(AIMObject):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties alle proeven."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Proef"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
