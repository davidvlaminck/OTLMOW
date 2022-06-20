# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PU(AIMNaamObject, PuntGeometrie):
    """Abstracte klasse die allerhande stuureenheden groupeert (PLCs, controllers, etc.)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)
