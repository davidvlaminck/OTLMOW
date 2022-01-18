# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KlAIMToestand import KlAIMToestand


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMToestand(ABC, AttributeInfo):
    """Voegt een attribuut toe aan de subklasse dat de huidige stand in de levenscyclus van het object aangeeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._toestand = OTLAttribuut(field=KlAIMToestand,
                                      naam='toestand',
                                      label='toestand',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand',
                                      definition='Geeft de actuele stand in de levenscyclus van het object.')

    @property
    def toestand(self):
        """Geeft de actuele stand in de levenscyclus van het object."""
        return self._toestand.waarde

    @toestand.setter
    def toestand(self, value):
        self._toestand.set_waarde(value, owner=self)
