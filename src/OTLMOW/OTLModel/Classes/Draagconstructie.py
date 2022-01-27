# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draagconstructie(ABC):
    """Abstracte voor alle draagconstructies."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        pass
