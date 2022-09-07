# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.Communicatieapparatuur import Communicatieapparatuur
from OTLMOW.OTLModel.Classes.Abstracten.FirmwareObject import FirmwareObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class ZenderOntvangerToegang(Communicatieapparatuur, FirmwareObject):
    """Abstracte voor relaties van Zender,Ontvanger en Repeater met andere apparatuur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Communicatieapparatuur.__init__(self)
        FirmwareObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector')
