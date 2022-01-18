# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMDBStatus(ABC, AttributeInfo):
    """Voegt een attribuut toe aan de subklasse dat aangeeft of de asset zichtbaar is in de databank of (zacht) verwijderd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._isActief = OTLAttribuut(field=BooleanField,
                                      naam='isActief',
                                      label='is actief',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief',
                                      definition='Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem.')

    @property
    def isActief(self):
        """Geeft aan of het object actief kan gebruikt worden of (zacht) verwijderd is uit het asset beheer systeem."""
        return self._isActief.waarde

    @isActief.setter
    def isActief(self, value):
        self._isActief.set_waarde(value, owner=self)
