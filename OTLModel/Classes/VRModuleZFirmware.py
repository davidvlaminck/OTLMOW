from abc import abstractmethod
from OTLModel.Classes.VerkeersregelaarModule import VerkeersregelaarModule


# Generated with OTLClassCreator
class VRModuleZFirmware(VerkeersregelaarModule):
    """Abstracte voor modules zonder firmware van een verkeersregelaar."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleZFirmware"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
