# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEcoLooprichelType import KlEcoLooprichelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduiker(AIMObject):
    """Buis- of tunnelvormige doorgang voor water onder een weg, die is voorzien van een oeverstrook of van looprichels zodat kleinere diersoorten beschermd voor het verkeer kunnen doorsteken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.typeLooprichel = KeuzelijstField(naam="typeLooprichel",
                                              label="type looprichel",
                                              lijst=KlEcoLooprichelType(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker.typeLooprichel",
                                              definition="Type van looprichel in de ecoduiker.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Type van looprichel in de ecoduiker."""
