# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.Signalisatie import Signalisatie
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlKleurReflector import KlKleurReflector


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bebakening(Signalisatie, AIMObject):
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
                                                    definition='De kleur van de reflector stroomafwaarts.',
                                                    owner=self)

        self._kleurReflectorOplopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorOplopend',
                                                    label='kleur oplopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorOplopend',
                                                    definition='De kleur van de reflector stroomopwaarts.',
                                                    owner=self)

    @property
    def kleurReflectorAflopend(self):
        """De kleur van de reflector stroomafwaarts."""
        return self._kleurReflectorAflopend.get_waarde()

    @kleurReflectorAflopend.setter
    def kleurReflectorAflopend(self, value):
        self._kleurReflectorAflopend.set_waarde(value, owner=self)

    @property
    def kleurReflectorOplopend(self):
        """De kleur van de reflector stroomopwaarts."""
        return self._kleurReflectorOplopend.get_waarde()

    @kleurReflectorOplopend.setter
    def kleurReflectorOplopend(self, value):
        self._kleurReflectorOplopend.set_waarde(value, owner=self)
