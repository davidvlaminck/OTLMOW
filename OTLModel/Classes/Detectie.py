# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVriBewaking import KlVriBewaking


# Generated with OTLClassCreator. To modify: extend, do not edit
class Detectie(AIMNaamObject):
    """Abstracte voor de overige detecties, zijnde die die niet onder de groepen "niet weggebonden detecties", " weggebonden detecties" of "detectielussen" vallen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.soortBewaking = KeuzelijstField(naam="soortBewaking",
                                             label="soort bewaking",
                                             lijst=KlVriBewaking(),
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectie.soortBewaking",
                                             definition="Type bewaking van de detectie.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Type bewaking van de detectie."""
