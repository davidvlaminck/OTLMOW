# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlPoEInjectorMerk import KlPoEInjectorMerk
from OTLModel.Datatypes.KlPoEInjectorModelnaam import KlPoEInjectorModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class PoEInjector(AIMNaamObject, AttributeInfo):
    """Een toestel waarmee stroom/voeding voor een ander toestel over een datakabel kan gestuurd worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._merk = OTLAttribuut(field=KlPoEInjectorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector.merk',
                                  definition='Het merk van de PoE-injector.')

        self._modelnaam = OTLAttribuut(field=KlPoEInjectorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector.modelnaam',
                                       definition='De modelnaam van de PoE-injector.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector.technischeFiche',
                                             definition='De technische fiche van de PoE-injector.')

    @property
    def merk(self):
        """Het merk van de PoE-injector."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de PoE-injector."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de PoE-injector."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
