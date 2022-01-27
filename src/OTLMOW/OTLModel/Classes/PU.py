# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class PU(AIMNaamObject):
    """Abstracte klasse die allerhande stuureenheden groupeert (PLCs, controllers, etc.)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
