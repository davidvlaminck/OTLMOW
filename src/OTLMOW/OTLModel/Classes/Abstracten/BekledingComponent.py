# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class BekledingComponent(AIMObject):
    """Abstracte voor componenten die als bekleding worden bevestigd op andere elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
