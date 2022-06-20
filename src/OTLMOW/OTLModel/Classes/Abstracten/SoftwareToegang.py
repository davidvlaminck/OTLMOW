# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SoftwareToegang(AIMNaamObject, GeenGeometrie):
    """Een abstracte waarmee een object kan connecteren naar software, al dan niet door gebruik te maken van de logische poort."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        GeenGeometrie.__init__(self)
