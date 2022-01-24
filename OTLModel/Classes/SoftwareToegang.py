# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class SoftwareToegang(AIMNaamObject):
    """Een abstracte waarmee een object kan connecteren naar software, al dan niet door gebruik te maken van de logische poort."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
