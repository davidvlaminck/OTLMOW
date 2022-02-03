# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlCodeklavierMerk import KlCodeklavierMerk
from OTLMOW.OTLModel.Datatypes.KlCodeklavierModelnaam import KlCodeklavierModelnaam
from OTLMOW.OTLModel.Datatypes.KlCodeklavierWerking import KlCodeklavierWerking
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Codeklavier(AIMNaamObject, PuntGeometrie):
    """Toestel voor het aansturen van een asset op basis van ingetoetste codes."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlCodeklavierMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.merk',
                                  definition='Het merk van het codeklavier.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCodeklavierModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.modelnaam',
                                       definition='De modelnaam van het codeklavier.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.technischeFiche',
                                             definition='De technische fiche van het codeklavier.',
                                             owner=self)

        self._werking = OTLAttribuut(field=KlCodeklavierWerking,
                                     naam='werking',
                                     label='werking',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.werking',
                                     definition='Indeling van het toestel volgens de manier waarop de gebruiker de aansturing doet.',
                                     owner=self)

    @property
    def merk(self):
        """Het merk van het codeklavier."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van het codeklavier."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van het codeklavier."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def werking(self):
        """Indeling van het toestel volgens de manier waarop de gebruiker de aansturing doet."""
        return self._werking.waarde

    @werking.setter
    def werking(self, value):
        self._werking.set_waarde(value, owner=self)
