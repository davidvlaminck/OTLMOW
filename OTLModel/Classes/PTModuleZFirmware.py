from abc import abstractmethod
from OTLModel.Classes.PTRegelaarModule import PTRegelaarModule


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTModuleZFirmware(PTRegelaarModule):
    """Abstracte voor de modules zonder firmware van het personentransportbeïnvloedingssysteem van een verkeersregelaar."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTModuleZFirmware"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
