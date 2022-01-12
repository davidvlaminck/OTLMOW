# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLantaarnLamptype import KlLantaarnLamptype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waarschuwingslantaarn(AIMNaamObject):
    """Abstracte voor waarschuwingsinrichtingen in de buurt van een verkeerslichtengeregeld kruispunt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.lamptype = KeuzelijstField(naam="lamptype",
                                        label="lamptype",
                                        lijst=KlLantaarnLamptype(),
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn.lamptype",
                                        definition="Type lamp in de lantaarn.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Type lamp in de lantaarn."""
