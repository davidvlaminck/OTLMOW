# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AOWSType import AOWSType
from OTLMOW.OTLModel.Classes.Markering import Markering
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkeringToegang(AOWSType, Markering, VlakGeometrie):
    """Abstracte als toegang tot de verschillende soorten dwarse markeringen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DwarseMarkeringToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AOWSType.__init__(self)
        Markering.__init__(self)
        VlakGeometrie.__init__(self)
