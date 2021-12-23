from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKleurReflector import KlKleurReflector


# Generated with OTLClassCreator
class Bebakening(AIMObject, Signalisatie):
    """Abstracte voor de bebakeningen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)
        self.kleurReflectorAflopend = KeuzelijstField(naam="kleurReflectorAflopend",
                                                      label="kleur aflopend",
                                                      lijst=KlKleurReflector(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorAflopend",
                                                      definition="De kleur van de reflector stroomafwaarts.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        """De kleur van de reflector stroomafwaarts."""

        self.kleurReflectorOplopend = KeuzelijstField(naam="kleurReflectorOplopend",
                                                      label="kleur oplopend",
                                                      lijst=KlKleurReflector(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorOplopend",
                                                      definition="De kleur van de reflector stroomopwaarts.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        """De kleur van de reflector stroomopwaarts."""
