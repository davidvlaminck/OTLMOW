# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.FirmwareObject import FirmwareObject
from OTLMOW.OTLModel.Classes.Abstracten.PTRegelaarModule import PTRegelaarModule


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTModuleMetFirmware(FirmwareObject, PTRegelaarModule):
    """Abstracte voor de modules met firmware van het personentransportbeïnvloedingssysteem van een verkeersregelaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTModuleMetFirmware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        FirmwareObject.__init__(self)
        PTRegelaarModule.__init__(self)
