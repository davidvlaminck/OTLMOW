# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlLantaarnLamptype import KlLantaarnLamptype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waarschuwingslantaarn(AIMNaamObject):
    """Abstracte voor waarschuwingsinrichtingen in de buurt van een verkeerslichtengeregeld kruispunt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._lamptype = OTLAttribuut(field=KlLantaarnLamptype,
                                      naam='lamptype',
                                      label='lamptype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn.lamptype',
                                      definition='Type lamp in de lantaarn.')

    @property
    def lamptype(self):
        """Type lamp in de lantaarn."""
        return self._lamptype.waarde

    @lamptype.setter
    def lamptype(self, value):
        self._lamptype.set_waarde(value, owner=self)
