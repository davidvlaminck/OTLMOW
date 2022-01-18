# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.VerkeersregelaarModule import VerkeersregelaarModule


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRModuleZFirmware(VerkeersregelaarModule, AttributeInfo):
    """Abstracte voor modules zonder firmware van een verkeersregelaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleZFirmware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AttributeInfo.__init__(self)
        VerkeersregelaarModule.__init__(self)
