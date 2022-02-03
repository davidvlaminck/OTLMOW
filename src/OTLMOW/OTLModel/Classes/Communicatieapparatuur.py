# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Communicatieapparatuur(AIMNaamObject, PuntGeometrie):
    """Abstracte voor alle benodigde apparatuur voor het ontvangen en verzenden van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Communicatieapparatuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)
