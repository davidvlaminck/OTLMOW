# coding=utf-8
from abc import abstractmethod, ABC
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelgeleidingEnLeidingBevestiging(LijnGeometrie):
    """Abstracte voor het bevestigen van kabelgeleidingen en leidingen aan bouwkundige elementen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        pass
