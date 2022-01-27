# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Classes.Signalisatie import Signalisatie
from src.OTLMOW.OTLModel.Datatypes.KlKleurReflector import KlKleurReflector


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bebakening(AIMObject, Signalisatie):
    """Abstracte voor de bebakeningen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        self._kleurReflectorAflopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorAflopend',
                                                    label='kleur aflopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorAflopend',
                                                    definition='De kleur van de reflector stroomafwaarts.')

        self._kleurReflectorOplopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorOplopend',
                                                    label='kleur oplopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorOplopend',
                                                    definition='De kleur van de reflector stroomopwaarts.')

    @property
    def kleurReflectorAflopend(self):
        """De kleur van de reflector stroomafwaarts."""
        return self._kleurReflectorAflopend.waarde

    @kleurReflectorAflopend.setter
    def kleurReflectorAflopend(self, value):
        self._kleurReflectorAflopend.set_waarde(value, owner=self)

    @property
    def kleurReflectorOplopend(self):
        """De kleur van de reflector stroomopwaarts."""
        return self._kleurReflectorOplopend.waarde

    @kleurReflectorOplopend.setter
    def kleurReflectorOplopend(self, value):
        self._kleurReflectorOplopend.set_waarde(value, owner=self)
