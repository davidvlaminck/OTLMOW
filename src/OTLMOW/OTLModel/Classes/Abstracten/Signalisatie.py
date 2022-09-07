# coding=utf-8
from abc import abstractmethod, ABC


# Generated with OTLClassCreator. To modify: extend, do not edit
class Signalisatie(ABC):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties van signalisatie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Signalisatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam')

        pass
