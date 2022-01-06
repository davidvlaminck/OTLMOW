# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.Communicatieapparatuur import Communicatieapparatuur
from OTLModel.Classes.FirmwareObject import FirmwareObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class ZenderOntvangerToegang(Communicatieapparatuur, FirmwareObject):
    """Abstracte voor relaties van Zender,Ontvanger en Repeater met andere apparatuur."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Communicatieapparatuur.__init__(self)
        FirmwareObject.__init__(self)
